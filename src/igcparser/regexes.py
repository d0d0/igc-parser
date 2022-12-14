RE_A = r"^A(\w{3})(\w{3,}?),*(?:FLIGHT:(\d+)|\:(.+))?$"
RE_A_1 = r"^A(\w{3})(.+)?$"
RE_HFDTE = r"^HFDTE(?:DATE:)?(\d{2})(\d{2})(\d{2})(?:,?(\d{2}))?"
RE_PLT_HEADER = r"^H(\w)PLT(?:.{0,}?:(.*)|(.*))$"
RE_CM2_HEADER = r"^H(\w)CM2(?:.{0,}?:(.*)|(.*))$"  # P is used by some broken Flarms
RE_GTY_HEADER = r"^H(\w)GTY(?:.{0,}?:(.*)|(.*))$"
RE_GID_HEADER = r"^H(\w)GID(?:.{0,}?:(.*)|(.*))$"
RE_CID_HEADER = r"^H(\w)CID(?:.{0,}?:(.*)|(.*))$"
RE_CCL_HEADER = r"^H(\w)CCL(?:.{0,}?:(.*)|(.*))$"
RE_SIT_HEADER = r"^H(\w)SIT(?:.{0,}?:(.*)|(.*))$"
RE_FTY_HEADER = r"^H(\w)FTY(?:.{0,}?:(.*)|(.*))$"
RE_RFW_HEADER = r"^H(\w)RFW(?:.{0,}?:(.*)|(.*))$"
RE_RHW_HEADER = r"^H(\w)RHW(?:.{0,}?:(.*)|(.*))$"
RE_B = r"^B(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{3})([NS])(\d{3})(\d{2})(\d{3})([EW])([AV])(-\d{4}|\d{5})(-\d{4}|\d{5})"  # noqa: E501
RE_K = r"^K(\d{2})(\d{2})(\d{2})"
RE_IJ = r"^[IJ](\d{2})(?:\d{2}\d{2}[A-Z]{3})+"
RE_TASK = r"^C(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{4})([-\d]{2})(.*)"
RE_TASKPOINT = r"^C(\d{2})(\d{2})(\d{3})([NS])(\d{3})(\d{2})(\d{3})([EW])(.*)"
