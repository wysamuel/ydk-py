


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'LptsPcbQuery_Enum' : _MetaInfoEnum('LptsPcbQuery_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper',
        {
            'all':'ALL',
            'static-policy':'STATIC_POLICY',
            'interface':'INTERFACE',
            'packet':'PACKET',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIcmpv6_Enum' : _MetaInfoEnum('MessageTypeIcmpv6_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper',
        {
            'destination-unreachable':'DESTINATION_UNREACHABLE',
            'packet-too-big':'PACKET_TOO_BIG',
            'time-exceeded':'TIME_EXCEEDED',
            'parameter-problem':'PARAMETER_PROBLEM',
            'echo-request':'ECHO_REQUEST',
            'echo-reply':'ECHO_REPLY',
            'multicast-listener-query':'MULTICAST_LISTENER_QUERY',
            'multicast-listener-report':'MULTICAST_LISTENER_REPORT',
            'multicast-listener-done':'MULTICAST_LISTENER_DONE',
            'router-solicitation':'ROUTER_SOLICITATION',
            'router-advertisement':'ROUTER_ADVERTISEMENT',
            'neighbor-solicitation':'NEIGHBOR_SOLICITATION',
            'neighbor-advertisement':'NEIGHBOR_ADVERTISEMENT',
            'redirect-message':'REDIRECT_MESSAGE',
            'router-renumbering':'ROUTER_RENUMBERING',
            'node-information-query':'NODE_INFORMATION_QUERY',
            'node-information-reply':'NODE_INFORMATION_REPLY',
            'inverse-neighbor-discovery-solicitaion':'INVERSE_NEIGHBOR_DISCOVERY_SOLICITAION',
            'inverse-neighbor-discover-advertisement':'INVERSE_NEIGHBOR_DISCOVER_ADVERTISEMENT',
            'v2-multicast-listener-report':'V2_MULTICAST_LISTENER_REPORT',
            'home-agent-address-discovery-request':'HOME_AGENT_ADDRESS_DISCOVERY_REQUEST',
            'home-agent-address-discovery-reply':'HOME_AGENT_ADDRESS_DISCOVERY_REPLY',
            'mobile-prefix-solicitation':'MOBILE_PREFIX_SOLICITATION',
            'mobile-prefix-advertisement':'MOBILE_PREFIX_ADVERTISEMENT',
            'certification-path-solicitation-message':'CERTIFICATION_PATH_SOLICITATION_MESSAGE',
            'certification-path-advertisement-message':'CERTIFICATION_PATH_ADVERTISEMENT_MESSAGE',
            'experimental-mobility-protocols':'EXPERIMENTAL_MOBILITY_PROTOCOLS',
            'multicast-router-advertisement':'MULTICAST_ROUTER_ADVERTISEMENT',
            'multicast-router-solicitation':'MULTICAST_ROUTER_SOLICITATION',
            'multicast-router-termination':'MULTICAST_ROUTER_TERMINATION',
            'fmipv6-messages':'FMIPV6_MESSAGES',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIcmp_Enum' : _MetaInfoEnum('MessageTypeIcmp_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper',
        {
            'echo-reply':'ECHO_REPLY',
            'destination-unreachable':'DESTINATION_UNREACHABLE',
            'source-quench':'SOURCE_QUENCH',
            'redirect':'REDIRECT',
            'alternate-host-address':'ALTERNATE_HOST_ADDRESS',
            'echo':'ECHO',
            'router-advertisement':'ROUTER_ADVERTISEMENT',
            'router-selection':'ROUTER_SELECTION',
            'time-exceeded':'TIME_EXCEEDED',
            'parameter-problem':'PARAMETER_PROBLEM',
            'time-stamp':'TIME_STAMP',
            'time-stamp-reply':'TIME_STAMP_REPLY',
            'information-request':'INFORMATION_REQUEST',
            'information-reply':'INFORMATION_REPLY',
            'address-mask-request':'ADDRESS_MASK_REQUEST',
            'address-mask-reply':'ADDRESS_MASK_REPLY',
            'trace-route':'TRACE_ROUTE',
            'datagram-conversion-error':'DATAGRAM_CONVERSION_ERROR',
            'mobile-host-redirect':'MOBILE_HOST_REDIRECT',
            'where-are-you':'WHERE_ARE_YOU',
            'iam-here':'IAM_HERE',
            'mobile-registration-request':'MOBILE_REGISTRATION_REQUEST',
            'mobile-registration-reply':'MOBILE_REGISTRATION_REPLY',
            'domain-name-request':'DOMAIN_NAME_REQUEST',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIgmp_Enum' : _MetaInfoEnum('MessageTypeIgmp_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper',
        {
            'membership-query':'MEMBERSHIP_QUERY',
            'v1-membership-report':'V1_MEMBERSHIP_REPORT',
            'dvmrp':'DVMRP',
            'pi-mv1':'PI_MV1',
            'cisco-trace-messages':'CISCO_TRACE_MESSAGES',
            'v2-membership-report':'V2_MEMBERSHIP_REPORT',
            'v2-leave-group':'V2_LEAVE_GROUP',
            'multicast-traceroute-response':'MULTICAST_TRACEROUTE_RESPONSE',
            'multicast-traceroute':'MULTICAST_TRACEROUTE',
            'v3-membership-report':'V3_MEMBERSHIP_REPORT',
            'multicast-router-advertisement':'MULTICAST_ROUTER_ADVERTISEMENT',
            'multicast-router-solicitation':'MULTICAST_ROUTER_SOLICITATION',
            'multicast-router-termination':'MULTICAST_ROUTER_TERMINATION',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIgmp_Enum' : _MetaInfoEnum('MessageTypeIgmp_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper',
        {
            'membership-query':'MEMBERSHIP_QUERY',
            'v1-membership-report':'V1_MEMBERSHIP_REPORT',
            'dvmrp':'DVMRP',
            'pi-mv1':'PI_MV1',
            'cisco-trace-messages':'CISCO_TRACE_MESSAGES',
            'v2-membership-report':'V2_MEMBERSHIP_REPORT',
            'v2-leave-group':'V2_LEAVE_GROUP',
            'multicast-traceroute-response':'MULTICAST_TRACEROUTE_RESPONSE',
            'multicast-traceroute':'MULTICAST_TRACEROUTE',
            'v3-membership-report':'V3_MEMBERSHIP_REPORT',
            'multicast-router-advertisement':'MULTICAST_ROUTER_ADVERTISEMENT',
            'multicast-router-solicitation':'MULTICAST_ROUTER_SOLICITATION',
            'multicast-router-termination':'MULTICAST_ROUTER_TERMINATION',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'Packet_Enum' : _MetaInfoEnum('Packet_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper',
        {
            'icmp':'ICMP',
            'icm-pv6':'ICM_PV6',
            'igmp':'IGMP',
            'unknown':'UNKNOWN',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIcmp_Enum' : _MetaInfoEnum('MessageTypeIcmp_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper',
        {
            'echo-reply':'ECHO_REPLY',
            'destination-unreachable':'DESTINATION_UNREACHABLE',
            'source-quench':'SOURCE_QUENCH',
            'redirect':'REDIRECT',
            'alternate-host-address':'ALTERNATE_HOST_ADDRESS',
            'echo':'ECHO',
            'router-advertisement':'ROUTER_ADVERTISEMENT',
            'router-selection':'ROUTER_SELECTION',
            'time-exceeded':'TIME_EXCEEDED',
            'parameter-problem':'PARAMETER_PROBLEM',
            'time-stamp':'TIME_STAMP',
            'time-stamp-reply':'TIME_STAMP_REPLY',
            'information-request':'INFORMATION_REQUEST',
            'information-reply':'INFORMATION_REPLY',
            'address-mask-request':'ADDRESS_MASK_REQUEST',
            'address-mask-reply':'ADDRESS_MASK_REPLY',
            'trace-route':'TRACE_ROUTE',
            'datagram-conversion-error':'DATAGRAM_CONVERSION_ERROR',
            'mobile-host-redirect':'MOBILE_HOST_REDIRECT',
            'where-are-you':'WHERE_ARE_YOU',
            'iam-here':'IAM_HERE',
            'mobile-registration-request':'MOBILE_REGISTRATION_REQUEST',
            'mobile-registration-reply':'MOBILE_REGISTRATION_REPLY',
            'domain-name-request':'DOMAIN_NAME_REQUEST',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'AddrFamily_Enum' : _MetaInfoEnum('AddrFamily_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper',
        {
            'unspecified':'UNSPECIFIED',
            'local':'LOCAL',
            'inet':'INET',
            'implink':'IMPLINK',
            'pup':'PUP',
            'chaos':'CHAOS',
            'ns':'NS',
            'iso':'ISO',
            'ecma':'ECMA',
            'data-kit':'DATA_KIT',
            'ccitt':'CCITT',
            'sna':'SNA',
            'de-cnet':'DE_CNET',
            'dli':'DLI',
            'lat':'LAT',
            'hylink':'HYLINK',
            'appletalk':'APPLETALK',
            'route':'ROUTE',
            'link':'LINK',
            'pseudo-xtp':'PSEUDO_XTP',
            'coip':'COIP',
            'cnt':'CNT',
            'pseudo-rtip':'PSEUDO_RTIP',
            'ipx':'IPX',
            'sip':'SIP',
            'pseudo-pip':'PSEUDO_PIP',
            'inet6':'INET6',
            'snap':'SNAP',
            'clnl':'CLNL',
            'chdlc':'CHDLC',
            'ppp':'PPP',
            'host-cas':'HOST_CAS',
            'dsp':'DSP',
            'sap':'SAP',
            'atm':'ATM',
            'fr':'FR',
            'mso':'MSO',
            'dchan':'DCHAN',
            'cas':'CAS',
            'nat':'NAT',
            'ether':'ETHER',
            'srp':'SRP',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'UdpAddressFamily_Enum' : _MetaInfoEnum('UdpAddressFamily_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper',
        {
            'ipv4':'IPV4',
            'ipv6':'IPV6',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIcmpv6_Enum' : _MetaInfoEnum('MessageTypeIcmpv6_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper',
        {
            'destination-unreachable':'DESTINATION_UNREACHABLE',
            'packet-too-big':'PACKET_TOO_BIG',
            'time-exceeded':'TIME_EXCEEDED',
            'parameter-problem':'PARAMETER_PROBLEM',
            'echo-request':'ECHO_REQUEST',
            'echo-reply':'ECHO_REPLY',
            'multicast-listener-query':'MULTICAST_LISTENER_QUERY',
            'multicast-listener-report':'MULTICAST_LISTENER_REPORT',
            'multicast-listener-done':'MULTICAST_LISTENER_DONE',
            'router-solicitation':'ROUTER_SOLICITATION',
            'router-advertisement':'ROUTER_ADVERTISEMENT',
            'neighbor-solicitation':'NEIGHBOR_SOLICITATION',
            'neighbor-advertisement':'NEIGHBOR_ADVERTISEMENT',
            'redirect-message':'REDIRECT_MESSAGE',
            'router-renumbering':'ROUTER_RENUMBERING',
            'node-information-query':'NODE_INFORMATION_QUERY',
            'node-information-reply':'NODE_INFORMATION_REPLY',
            'inverse-neighbor-discovery-solicitaion':'INVERSE_NEIGHBOR_DISCOVERY_SOLICITAION',
            'inverse-neighbor-discover-advertisement':'INVERSE_NEIGHBOR_DISCOVER_ADVERTISEMENT',
            'v2-multicast-listener-report':'V2_MULTICAST_LISTENER_REPORT',
            'home-agent-address-discovery-request':'HOME_AGENT_ADDRESS_DISCOVERY_REQUEST',
            'home-agent-address-discovery-reply':'HOME_AGENT_ADDRESS_DISCOVERY_REPLY',
            'mobile-prefix-solicitation':'MOBILE_PREFIX_SOLICITATION',
            'mobile-prefix-advertisement':'MOBILE_PREFIX_ADVERTISEMENT',
            'certification-path-solicitation-message':'CERTIFICATION_PATH_SOLICITATION_MESSAGE',
            'certification-path-advertisement-message':'CERTIFICATION_PATH_ADVERTISEMENT_MESSAGE',
            'experimental-mobility-protocols':'EXPERIMENTAL_MOBILITY_PROTOCOLS',
            'multicast-router-advertisement':'MULTICAST_ROUTER_ADVERTISEMENT',
            'multicast-router-solicitation':'MULTICAST_ROUTER_SOLICITATION',
            'multicast-router-termination':'MULTICAST_ROUTER_TERMINATION',
            'fmipv6-messages':'FMIPV6_MESSAGES',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'Udp.Nodes.Node.Statistics.Ipv4Traffic' : {
        'meta_info' : _MetaInfoClass('Udp.Nodes.Node.Statistics.Ipv4Traffic',
            False, 
            [
            _MetaInfoClassMember('udp-bad-length-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP bad length
                ''',
                'udp_bad_length_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-checksum-error-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP Checksum Errors
                ''',
                'udp_checksum_error_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP drop for other reason
                ''',
                'udp_dropped_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-input-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP Received
                ''',
                'udp_input_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-no-port-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP No Port
                ''',
                'udp_no_port_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-output-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP Transmitted
                ''',
                'udp_output_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'ipv4-traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'Udp.Nodes.Node.Statistics.Ipv6Traffic' : {
        'meta_info' : _MetaInfoClass('Udp.Nodes.Node.Statistics.Ipv6Traffic',
            False, 
            [
            _MetaInfoClassMember('udp-bad-length-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP bad length
                ''',
                'udp_bad_length_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-checksum-error-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP Checksum Errors
                ''',
                'udp_checksum_error_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP drop for other reason
                ''',
                'udp_dropped_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-input-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP Received
                ''',
                'udp_input_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-no-port-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP No Port
                ''',
                'udp_no_port_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-output-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                UDP Transmitted
                ''',
                'udp_output_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'ipv6-traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'Udp.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('Udp.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('ipv4-traffic', REFERENCE_CLASS, 'Ipv4Traffic' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'Udp.Nodes.Node.Statistics.Ipv4Traffic', 
                [], [], 
                '''                UDP Traffic statistics for IPv4
                ''',
                'ipv4_traffic',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-traffic', REFERENCE_CLASS, 'Ipv6Traffic' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'Udp.Nodes.Node.Statistics.Ipv6Traffic', 
                [], [], 
                '''                UDP Traffic statistics for IPv6
                ''',
                'ipv6_traffic',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'Udp.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Udp.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'Udp.Nodes.Node.Statistics', 
                [], [], 
                '''                Statistical UDP operational data for a node
                ''',
                'statistics',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'Udp.Nodes' : {
        'meta_info' : _MetaInfoClass('Udp.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'Udp.Nodes.Node', 
                [], [], 
                '''                UDP operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'Udp' : {
        'meta_info' : _MetaInfoClass('Udp',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'Udp.Nodes', 
                [], [], 
                '''                Node-specific UDP operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'udp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask',
            False, 
            [
            _MetaInfoClassMember('is-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set interface
                ''',
                'is_interface',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-local-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Local Address
                ''',
                'is_local_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-local-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Local Port
                ''',
                'is_local_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-packet-type', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set packet type
                ''',
                'is_packet_type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-remote-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Remote address
                ''',
                'is_remote_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-remote-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Remote Port
                ''',
                'is_remote_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'accept-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'AddrFamily_Enum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType',
            False, 
            [
            _MetaInfoClassMember('icm-pv6-message-type', REFERENCE_ENUM_CLASS, 'MessageTypeIcmpv6_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'MessageTypeIcmpv6_Enum', 
                [], [], 
                '''                ICMPv6 message type
                ''',
                'icm_pv6_message_type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('icmp-message-type', REFERENCE_ENUM_CLASS, 'MessageTypeIcmp_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'MessageTypeIcmp_Enum', 
                [], [], 
                '''                ICMP message type
                ''',
                'icmp_message_type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('igmp-message-type', REFERENCE_ENUM_CLASS, 'MessageTypeIgmp_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'MessageTypeIgmp_Enum', 
                [], [], 
                '''                IGMP message type
                ''',
                'igmp_message_type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('message-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Message type in number
                ''',
                'message_id',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Packet_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'Packet_Enum', 
                [], [], 
                '''                Type
                ''',
                'type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'packet-type',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'AddrFamily_Enum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'remote-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter',
            False, 
            [
            _MetaInfoClassMember('flow-types-info', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                flow information
                ''',
                'flow_types_info',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress', 
                [], [], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Local address length
                ''',
                'local_length',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('packet-type', REFERENCE_CLASS, 'PacketType' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType', 
                [], [], 
                '''                Protocol-specific packet type
                ''',
                'packet_type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('receive-local-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Receive Local port
                ''',
                'receive_local_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('receive-remote-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Receive Remote port
                ''',
                'receive_remote_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('remote-address', REFERENCE_CLASS, 'RemoteAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress', 
                [], [], 
                '''                Remote address
                ''',
                'remote_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('remote-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Remote address length
                ''',
                'remote_length',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Minimum TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags',
            False, 
            [
            _MetaInfoClassMember('is-ignore-vrf-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore VRF Filter
                ''',
                'is_ignore_vrf_filter',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-local-address-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sent drop packets
                ''',
                'is_local_address_ignore',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-pcb-bound', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCB bound
                ''',
                'is_pcb_bound',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'lpts-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options',
            False, 
            [
            _MetaInfoClassMember('is-ip-sla', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IP SLA
                ''',
                'is_ip_sla',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-receive-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Receive filter enabled
                ''',
                'is_receive_filter',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'options',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb',
            False, 
            [
            _MetaInfoClassMember('accept-mask', REFERENCE_CLASS, 'AcceptMask' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask', 
                [], [], 
                '''                AcceptMask
                ''',
                'accept_mask',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter', 
                [], [], 
                '''                Interface Filters
                ''',
                'filter',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('flow-types-info', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                flow information
                ''',
                'flow_types_info',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('lpts-flags', REFERENCE_CLASS, 'LptsFlags' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags', 
                [], [], 
                '''                LPTS flags
                ''',
                'lpts_flags',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options', 
                [], [], 
                '''                Receive options
                ''',
                'options',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Minimum TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'lpts-pcb',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'AddrFamily_Enum', 
                [], [], 
                '''                Address Family
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('lpts-pcb', REFERENCE_CLASS, 'LptsPcb' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb', 
                [], [], 
                '''                LPTS PCB information
                ''',
                'lpts_pcb',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'common',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'AddrFamily_Enum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'foreign-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'AddrFamily_Enum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb',
            False, 
            [
            _MetaInfoClassMember('pcb-address', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                PCB address
                ''',
                'pcb_address',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('common', REFERENCE_CLASS, 'Common' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common', 
                [], [], 
                '''                Common PCB information
                ''',
                'common',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_CLASS, 'ForeignAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress', 
                [], [], 
                '''                Remote IP address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Remote port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('l4-protocol', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Layer 4 protocol
                ''',
                'l4_protocol',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress', 
                [], [], 
                '''                Local IP address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs',
            False, 
            [
            _MetaInfoClassMember('pcb', REFERENCE_LIST, 'Pcb' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb', 
                [], [], 
                '''                A PCB information
                ''',
                'pcb',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcbs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query',
            False, 
            [
            _MetaInfoClassMember('query-name', REFERENCE_ENUM_CLASS, 'LptsPcbQuery_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'LptsPcbQuery_Enum', 
                [], [], 
                '''                Query option
                ''',
                'query_name',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('pcbs', REFERENCE_CLASS, 'Pcbs' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs', 
                [], [], 
                '''                List of PCBs
                ''',
                'pcbs',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'query',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries',
            False, 
            [
            _MetaInfoClassMember('query', REFERENCE_LIST, 'Query' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query', 
                [], [], 
                '''                Query option
                ''',
                'query',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'queries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts',
            False, 
            [
            _MetaInfoClassMember('queries', REFERENCE_CLASS, 'Queries' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries', 
                [], [], 
                '''                List of query options
                ''',
                'queries',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'lpts',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily_Enum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'foreign-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily_Enum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbBriefs.PcbBrief',
            False, 
            [
            _MetaInfoClassMember('pcb-address', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Protocol Control Block address
                ''',
                'pcb_address',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily_Enum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_CLASS, 'ForeignAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress', 
                [], [], 
                '''                Foreign address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Foreign port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress', 
                [], [], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('receive-queue', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Receive queue count
                ''',
                'receive_queue',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('send-queue', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Send queue count
                ''',
                'send_queue',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbBriefs' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbBriefs',
            False, 
            [
            _MetaInfoClassMember('pcb-brief', REFERENCE_LIST, 'PcbBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief', 
                [], [], 
                '''                Brief information about a UDP connection
                ''',
                'pcb_brief',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily_Enum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'foreign-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily_Enum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbDetails.PcbDetail' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbDetails.PcbDetail',
            False, 
            [
            _MetaInfoClassMember('pcb-address', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Protocol Control Block address
                ''',
                'pcb_address',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamily_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily_Enum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_CLASS, 'ForeignAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress', 
                [], [], 
                '''                Foreign address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Foreign port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress', 
                [], [], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-process-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ID of local process
                ''',
                'local_process_id',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('receive-queue', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Receive queue count
                ''',
                'receive_queue',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('send-queue', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Send queue count
                ''',
                'send_queue',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbDetails' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbDetails',
            False, 
            [
            _MetaInfoClassMember('pcb-detail', REFERENCE_LIST, 'PcbDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbDetails.PcbDetail', 
                [], [], 
                '''                Detail information about a UDP connection
                ''',
                'pcb_detail',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.Clients.Client' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Displaying client's aggregated statistics
                ''',
                'client_id',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('client-jid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Job ID of the transport client
                ''',
                'client_jid',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 21)], [], 
                '''                Transport client name
                ''',
                'client_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-received-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total IPv4 packets received from client
                ''',
                'ipv4_received_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total IPv4 packets sent to client
                ''',
                'ipv4_sent_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-received-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total IPv6 packets received from app
                ''',
                'ipv6_received_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total IPv6 packets sent to app
                ''',
                'ipv6_sent_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.Clients' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.Clients.Client', 
                [], [], 
                '''                Describing Client ID
                ''',
                'client',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive',
            False, 
            [
            _MetaInfoClassMember('failed-queued-application-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Packets failed queued to application
                ''',
                'failed_queued_application_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('failed-queued-application-socket-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Packet that couldn't be queued to application.on
                socket
                ''',
                'failed_queued_application_socket_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('queued-application-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Packets queued to application
                ''',
                'queued_application_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('queued-application-socket-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Packets queued to application on socket
                ''',
                'queued_application_socket_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-network-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Packets received from network
                ''',
                'received_network_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'receive',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send',
            False, 
            [
            _MetaInfoClassMember('failed-queued-net-io-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Packets failed getting queued to network (NetIO)
                ''',
                'failed_queued_net_io_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('failed-queued-network-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Packets failed getting queued to network (v4/v6
                IO)
                ''',
                'failed_queued_network_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-application-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Bytes received from application
                ''',
                'received_application_bytes',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-xipc-pulses', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                XIPC pulses received from application
                ''',
                'received_xipc_pulses',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('sent-net-io-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Packets sent to network (NetIO)
                ''',
                'sent_net_io_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('sent-network-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Packets sent to network (v4/v6 IO)
                ''',
                'sent_network_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'send',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic',
            False, 
            [
            _MetaInfoClassMember('pcb-address', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Protocol Control Block address
                ''',
                'pcb_address',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('is-paw-socket', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if paw socket
                ''',
                'is_paw_socket',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('receive', REFERENCE_CLASS, 'Receive' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive', 
                [], [], 
                '''                UDP receive statistics
                ''',
                'receive',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('send', REFERENCE_CLASS, 'Send' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send', 
                [], [], 
                '''                UDP send statistics
                ''',
                'send',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.PcbStatistics' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.PcbStatistics',
            False, 
            [
            _MetaInfoClassMember('pcb-statistic', REFERENCE_LIST, 'PcbStatistic' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic', 
                [], [], 
                '''                Satistics associated with a particular PCB
                ''',
                'pcb_statistic',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.Summary' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.Summary',
            False, 
            [
            _MetaInfoClassMember('cloned-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total cloned packets
                ''',
                'cloned_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('failed-clone-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total failed cloned packets
                ''',
                'failed_clone_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('forward-broadcast-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total forwarding broadcast packets
                ''',
                'forward_broadcast_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-bad-checksum-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Packets received has bad checksum
                ''',
                'received_bad_checksum_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-drop-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Packets dropped for other reasons
                ''',
                'received_drop_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-no-port-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Packets received when no wild listener
                ''',
                'received_no_port_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-too-short-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Packets received is too short
                ''',
                'received_too_short_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-total-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total packets received
                ''',
                'received_total_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('sent-error-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total send erorr packets
                ''',
                'sent_error_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('sent-total-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total packets sent
                ''',
                'sent_total_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.Clients', 
                [], [], 
                '''                Table listing clients
                ''',
                'clients',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('pcb-statistics', REFERENCE_CLASS, 'PcbStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.PcbStatistics', 
                [], [], 
                '''                Table listing the UDP connections for which
                statistics are provided
                ''',
                'pcb_statistics',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.Summary', 
                [], [], 
                '''                Summary statistics across all UDP connections
                ''',
                'summary',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('lpts', REFERENCE_CLASS, 'Lpts' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts', 
                [], [], 
                '''                LPTS statistical data
                ''',
                'lpts',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('pcb-briefs', REFERENCE_CLASS, 'PcbBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbBriefs', 
                [], [], 
                '''                Brief information for list of UDP connections.
                ''',
                'pcb_briefs',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('pcb-details', REFERENCE_CLASS, 'PcbDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbDetails', 
                [], [], 
                '''                Detail information for list of UDP connections
                .
                ''',
                'pcb_details',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics', 
                [], [], 
                '''                Statistics of UDP connections
                ''',
                'statistics',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node', 
                [], [], 
                '''                Information about a particular node
                ''',
                'node',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection' : {
        'meta_info' : _MetaInfoClass('UdpConnection',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes', 
                [], [], 
                '''                List of UDP connections nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'udp-connection',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
}
_meta_table['Udp.Nodes.Node.Statistics.Ipv4Traffic']['meta_info'].parent =_meta_table['Udp.Nodes.Node.Statistics']['meta_info']
_meta_table['Udp.Nodes.Node.Statistics.Ipv6Traffic']['meta_info'].parent =_meta_table['Udp.Nodes.Node.Statistics']['meta_info']
_meta_table['Udp.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['Udp.Nodes.Node']['meta_info']
_meta_table['Udp.Nodes.Node']['meta_info'].parent =_meta_table['Udp.Nodes']['meta_info']
_meta_table['Udp.Nodes']['meta_info'].parent =_meta_table['Udp']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbBriefs']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbDetails']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.Clients.Client']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics.Clients']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.Clients']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.Summary']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbBriefs']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbDetails']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node']['meta_info']
_meta_table['UdpConnection.Nodes.Node']['meta_info'].parent =_meta_table['UdpConnection.Nodes']['meta_info']
_meta_table['UdpConnection.Nodes']['meta_info'].parent =_meta_table['UdpConnection']['meta_info']