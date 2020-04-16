# =============================================================================
# Minet CrowdTangle Exceptions.
# =============================================================================
#
from minet.exceptions import MinetError


class CrowdTangleError(MinetError):
    pass


class CrowdTangleMissingTokenError(CrowdTangleError):
    pass
