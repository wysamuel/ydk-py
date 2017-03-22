


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'DynTmplMulticastModeEnum' : _MetaInfoEnum('DynTmplMulticastModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg',
        {
            'qos-correlation':'qos_correlation',
            'passive':'passive',
        }, 'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg']),
}
