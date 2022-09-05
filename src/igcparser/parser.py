import datetime
import re
from pathlib import Path
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from .enums import ARecord
from .enums import BRecord
from .enums import Flight
from .enums import KRecord
from .enums import RecordExtension
from .regexes import RE_A
from .regexes import RE_A_1
from .regexes import RE_B
from .regexes import RE_HFDTE
from .regexes import RE_IJ
from .regexes import RE_K


class IgcParser:
    @staticmethod
    def parse(file_path: Union[str, Path]) -> Flight:
        path: Path = Path(file_path)

        if not path.exists():
            raise Exception("Path does not exist.")

        with open(path) as f:
            return IgcParser._parse_lines([line.strip() for line in f.readlines()])

    @staticmethod
    def _parse_lines(lines: List[str]) -> Flight:
        flight: Flight = Flight()

        for line in lines:
            if line.startswith("C"):
                IgcParser._parse_task_line(line)

            if line.startswith("H"):
                IgcParser._parse_header(line)

            if line.startswith("A"):
                IgcParser._parse_a_record(line)

            if line.startswith("B"):
                flight.fixes.append(IgcParser._parse_b_record(line))

            if line.startswith("H"):
                pass

            if line.startswith("I") or line.startswith("J"):
                print(IgcParser._parse_ij_record(line))

        return Flight()

    @staticmethod
    def _parse_b_record(line: str) -> Optional[BRecord]:
        if match := re.match(RE_B, line, flags=re.IGNORECASE):
            latitude_degrees: float = int(match.group(4)) + (int(match.group(5)) + int(match.group(6)) / 100) / 60
            longitude_degrees: float = int(match.group(8)) + (int(match.group(9)) + int(match.group(10)) / 100) / 60
            return BRecord(
                time=datetime.time(
                    hour=int(match.group(1)),
                    minute=int(match.group(2)),
                    second=int(match.group(3)),
                ),
                latitude=-latitude_degrees if match.group(7) == "S" else latitude_degrees,
                longitude=-longitude_degrees if match.group(11) == "W" else longitude_degrees,
                valid=match.group(12) == "A",
                pressure_altitude=None if match.group(13) == "0000" else int(match.group(13)),
                gps_altitude=None if match.group(14) == "0000" else int(match.group(14)),
            )

        return None

    @staticmethod
    def _parse_a_record(line: str) -> Optional[ARecord]:
        if match := re.match(RE_A, line, flags=re.IGNORECASE):
            return ARecord(
                manufacturer=match.group(1),
                logger_id=match.group(2),
                num_flight=int(match.group(3)) if match.group(3) else None,
                additional_data=match.group(4) or None,
            )

        if match := re.match(RE_A_1, line, flags=re.IGNORECASE):
            return ARecord(
                manufacturer=match.group(1),
                logger_id=None,
                num_flight=None,
                additional_data=match.group(2) or None,
            )

        return None

    @staticmethod
    def _parse_ij_record(line: str) -> List[RecordExtension]:
        result: List[RecordExtension] = []
        if match := re.match(RE_IJ, line, flags=re.IGNORECASE):
            num: int = int(match.group(1))
            if len(line) < 3 + num * 7:
                raise Exception

            for i in range(num):
                offset: int = 3 + i * 7
                result.append(
                    RecordExtension(
                        start=int(line[offset : offset + 2]) - 1,
                        length=int(line[offset + 2 : offset + 4]) - 1,
                        code=line[offset + 4 : offset + 7],
                    )
                )

        return result

    @staticmethod
    def parse_k_record(line: str) -> Optional[KRecord]:
        if match := re.match(RE_K, line, flags=re.IGNORECASE):
            return KRecord(
                time=datetime.time(
                    hour=int(match.group(1)),
                    minute=int(match.group(2)),
                    second=int(match.group(3)),
                )
            )

        return None

    @staticmethod
    def _parse_header(line: str):
        def _parse_date_header() -> Tuple[datetime.date, Optional[int]]:
            if match := re.match(RE_HFDTE, line, flags=re.IGNORECASE):
                century: str = "19" if match[3][0] in ("8", "9") else "20"

                num_flight: Optional[int] = int(match[4]) if match[4] else None
                return datetime.date(year=int(century + match[3]), month=int(match[2]), day=int(match[1])), num_flight

        header_type: str = line[2:5]

        if header_type == "DTE":
            date, num_flight = _parse_date_header()

        if header_type == "PLT":
            pass

        pass

    @staticmethod
    def _parse_task_line(line):
        pass
