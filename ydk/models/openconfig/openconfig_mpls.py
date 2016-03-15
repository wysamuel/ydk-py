""" openconfig_mpls 

This module provides data definitions for configuration of
Multiprotocol Label Switching (MPLS) and associated protocols for
signaling and traffic engineering.

RFC 3031\: Multiprotocol Label Switching Architecture

The MPLS / TE data model consists of several modules and
submodules as shown below.  The top\-level MPLS module describes
the overall framework.  Three types of LSPs are supported\:

i) traffic\-engineered (or constrained\-path)

ii) IGP\-congruent (LSPs that follow the IGP path)

iii) static LSPs which are not signaled

The structure of each of these LSP configurations is defined in
corresponding submodules.  Companion modules define the relevant
configuration and operational data specific to key signaling
protocols used in operational practice.


                         +\-\-\-\-\-\-\-+
       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\->\| MPLS  \|<\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
       \|                 +\-\-\-\-\-\-\-+               \|
       \|                     ^                   \|
       \|                     \|                   \|
  +\-\-\-\-+\-\-\-\-\-+      +\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+     +\-\-\-\-\-+\-\-\-\-\-+
  \| TE LSPs  \|      \| IGP\-based LSPs \|     \|static LSPs\|
  \|          \|      \|                \|     \|           \|
  +\-\-\-\-\-\-\-\-\-\-+      +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     +\-\-\-\-\-\-\-\-\-\-\-+
      ^  ^                    ^  ^
      \|  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+   \|  +\-\-\-\-\-\-\-\-+
      \|                   \|   \|           \|
      \|   +\-\-\-\-\-\-+      +\-+\-\-\-+\-+      +\-\-+\-\-+
      +\-\-\-+ RSVP \|      \|SEGMENT\|      \| LDP \|
          +\-\-\-\-\-\-+      \|ROUTING\|      +\-\-\-\-\-+
                        +\-\-\-\-\-\-\-+


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.openconfig.openconfig_mpls_types import LspOperStatus_Identity
from ydk.models.openconfig.openconfig_mpls_types import LspRole_Identity
from ydk.models.openconfig.openconfig_mpls_types import NullLabelType_Identity
from ydk.models.openconfig.openconfig_mpls_types import ProtectionType_Identity
from ydk.models.openconfig.openconfig_mpls_types import TunnelAdminStatus_Identity
from ydk.models.openconfig.openconfig_mpls_types import TunnelType_Enum
from ydk.models.openconfig.openconfig_mpls_types import TunnelType_Identity

class CspfTieBreaking_Enum(Enum):
    """
    CspfTieBreaking_Enum

    type to indicate the CSPF selection policy when
    multiple equal cost paths are available

    """

    """

    CSPF calculation selects a random path among
    multiple equal\-cost paths to the destination

    """
    RANDOM = 0

    """

    CSPF calculation selects the path with greatest
    available bandwidth

    """
    LEAST_FILL = 1

    """

    CSPF calculation selects the path with the least
    available bandwidth

    """
    MOST_FILL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls as meta
        return meta._meta_table['CspfTieBreaking_Enum']


class MplsHopType_Enum(Enum):
    """
    MplsHopType_Enum

    enumerated type for specifying loose or strict
    paths

    """

    """

    loose hop in an explicit path

    """
    LOOSE = 0

    """

    strict hop in an explicit path

    """
    STRICT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls as meta
        return meta._meta_table['MplsHopType_Enum']


class MplsSrlgFloodingType_Enum(Enum):
    """
    MplsSrlgFloodingType_Enum

    Enumerated bype for specifying how the SRLG is flooded

    """

    """

    SRLG is flooded in the IGP

    """
    FLOODED_SRLG = 0

    """

    SRLG is not flooded, the members are
    statically configured

    """
    STATIC_SRLG = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls as meta
        return meta._meta_table['MplsSrlgFloodingType_Enum']


class TeBandwidthType_Enum(Enum):
    """
    TeBandwidthType_Enum

    enumerated type for specifying whether bandwidth is
    explicitly specified or automatically computed

    """

    """

    Bandwidth is explicitly specified

    """
    SPECIFIED = 0

    """

    Bandwidth is automatically computed

    """
    AUTO = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls as meta
        return meta._meta_table['TeBandwidthType_Enum']


class TeMetricType_Enum(Enum):
    """
    TeMetricType_Enum

    union type for setting the LSP TE metric to a
    static value, or to track the IGP metric

    """

    """

    set the LSP metric to track the underlying
    IGP metric

    """
    IGP = 0


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls as meta
        return meta._meta_table['TeMetricType_Enum']



class Mpls(object):
    """
    Anchor point for mpls configuration and operational
    data
    
    .. attribute:: global_
    
    	general mpls configuration applicable to any type of LSP and signaling protocol \- label ranges, entropy label supportmay be added here
    	**type**\: :py:class:`Global <ydk.models.openconfig.openconfig_mpls.Mpls.Global>`
    
    .. attribute:: lsps
    
    	LSP definitions and configuration
    	**type**\: :py:class:`Lsps <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps>`
    
    .. attribute:: signaling_protocols
    
    	top\-level signaling protocol configuration
    	**type**\: :py:class:`SignalingProtocols <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols>`
    
    .. attribute:: te_global_attributes
    
    	traffic\-engineering global attributes
    	**type**\: :py:class:`TeGlobalAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes>`
    
    .. attribute:: te_interface_attributes
    
    	traffic engineering attributes specific for interfaces
    	**type**\: :py:class:`TeInterfaceAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'mpls'
    _revision = '2015-11-05'

    def __init__(self):
        self.global_ = Mpls.Global()
        self.global_.parent = self
        self.lsps = Mpls.Lsps()
        self.lsps.parent = self
        self.signaling_protocols = Mpls.SignalingProtocols()
        self.signaling_protocols.parent = self
        self.te_global_attributes = Mpls.TeGlobalAttributes()
        self.te_global_attributes.parent = self
        self.te_interface_attributes = Mpls.TeInterfaceAttributes()
        self.te_interface_attributes.parent = self


    class Global(object):
        """
        general mpls configuration applicable to any
        type of LSP and signaling protocol \- label ranges,
        entropy label supportmay be added here
        
        .. attribute:: config
        
        	Top level global MPLS configuration
        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Global.Config>`
        
        .. attribute:: mpls_interface_attributes
        
        	Parameters related to MPLS interfaces
        	**type**\: :py:class:`MplsInterfaceAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.Global.MplsInterfaceAttributes>`
        
        .. attribute:: state
        
        	Top level global MPLS state
        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Global.State>`
        
        

        """

        _prefix = 'mpls'
        _revision = '2015-11-05'

        def __init__(self):
            self.parent = None
            self.config = Mpls.Global.Config()
            self.config.parent = self
            self.mpls_interface_attributes = Mpls.Global.MplsInterfaceAttributes()
            self.mpls_interface_attributes.parent = self
            self.state = Mpls.Global.State()
            self.state.parent = self


        class Config(object):
            """
            Top level global MPLS configuration
            
            .. attribute:: null_label
            
            	The null\-label type used, implicit or explicit
            	**type**\: :py:class:`NullLabelType_Identity <ydk.models.openconfig.openconfig_mpls_types.NullLabelType_Identity>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.null_label = None

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:global/openconfig-mpls:config'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.null_label is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.Global.Config']['meta_info']


        class MplsInterfaceAttributes(object):
            """
            Parameters related to MPLS interfaces
            
            .. attribute:: interface
            
            	List of TE interfaces
            	**type**\: list of :py:class:`Interface <ydk.models.openconfig.openconfig_mpls.Mpls.Global.MplsInterfaceAttributes.Interface>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                List of TE interfaces
                
                .. attribute:: name
                
                	The interface name
                	**type**\: str
                
                .. attribute:: config
                
                	Configuration parameters related to MPLS interfaces\:
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Global.MplsInterfaceAttributes.Interface.Config>`
                
                .. attribute:: state
                
                	State parameters related to TE interfaces
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Global.MplsInterfaceAttributes.Interface.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.config = Mpls.Global.MplsInterfaceAttributes.Interface.Config()
                    self.config.parent = self
                    self.state = Mpls.Global.MplsInterfaceAttributes.Interface.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters related to MPLS interfaces\:
                    
                    .. attribute:: mpls_enabled
                    
                    	Enable MPLS forwarding on this interfacek
                    	**type**\: bool
                    
                    .. attribute:: name
                    
                    	reference to interface name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.mpls_enabled = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.mpls_enabled is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Global.MplsInterfaceAttributes.Interface.Config']['meta_info']


                class State(object):
                    """
                    State parameters related to TE interfaces
                    
                    .. attribute:: mpls_enabled
                    
                    	Enable MPLS forwarding on this interfacek
                    	**type**\: bool
                    
                    .. attribute:: name
                    
                    	reference to interface name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.mpls_enabled = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.mpls_enabled is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Global.MplsInterfaceAttributes.Interface.State']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return '/openconfig-mpls:mpls/openconfig-mpls:global/openconfig-mpls:mpls-interface-attributes/openconfig-mpls:interface[openconfig-mpls:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.config is not None and self.config.is_presence():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.Global.MplsInterfaceAttributes.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:global/openconfig-mpls:mpls-interface-attributes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.Global.MplsInterfaceAttributes']['meta_info']


        class State(object):
            """
            Top level global MPLS state
            
            .. attribute:: null_label
            
            	The null\-label type used, implicit or explicit
            	**type**\: :py:class:`NullLabelType_Identity <ydk.models.openconfig.openconfig_mpls_types.NullLabelType_Identity>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.null_label = None

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:global/openconfig-mpls:state'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.null_label is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.Global.State']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-mpls:mpls/openconfig-mpls:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.config is not None and self.config._has_data():
                return True

            if self.config is not None and self.config.is_presence():
                return True

            if self.mpls_interface_attributes is not None and self.mpls_interface_attributes._has_data():
                return True

            if self.mpls_interface_attributes is not None and self.mpls_interface_attributes.is_presence():
                return True

            if self.state is not None and self.state._has_data():
                return True

            if self.state is not None and self.state.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_mpls as meta
            return meta._meta_table['Mpls.Global']['meta_info']


    class Lsps(object):
        """
        LSP definitions and configuration
        
        .. attribute:: constrained_path
        
        	traffic\-engineered LSPs supporting different path computation and signaling methods
        	**type**\: :py:class:`ConstrainedPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath>`
        
        .. attribute:: static_lsps
        
        	statically configured LSPs, without dynamic signaling
        	**type**\: :py:class:`StaticLsps <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps>`
        
        .. attribute:: unconstrained_path
        
        	LSPs that use the IGP\-determined path, i.e., non traffic\-engineered, or non constrained\-path
        	**type**\: :py:class:`UnconstrainedPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath>`
        
        

        """

        _prefix = 'mpls'
        _revision = '2015-11-05'

        def __init__(self):
            self.parent = None
            self.constrained_path = Mpls.Lsps.ConstrainedPath()
            self.constrained_path.parent = self
            self.static_lsps = Mpls.Lsps.StaticLsps()
            self.static_lsps.parent = self
            self.unconstrained_path = Mpls.Lsps.UnconstrainedPath()
            self.unconstrained_path.parent = self


        class ConstrainedPath(object):
            """
            traffic\-engineered LSPs supporting different
            path computation and signaling methods
            
            .. attribute:: named_explicit_paths
            
            	A list of explicit paths
            	**type**\: list of :py:class:`NamedExplicitPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths>`
            
            .. attribute:: tunnel
            
            	List of TE tunnels
            	**type**\: list of :py:class:`Tunnel <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.named_explicit_paths = YList()
                self.named_explicit_paths.parent = self
                self.named_explicit_paths.name = 'named_explicit_paths'
                self.tunnel = YList()
                self.tunnel.parent = self
                self.tunnel.name = 'tunnel'


            class NamedExplicitPaths(object):
                """
                A list of explicit paths
                
                .. attribute:: name
                
                	A string name that uniquely identifies an explicit path
                	**type**\: str
                
                .. attribute:: config
                
                	Configuration parameters relating to named explicit paths
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config>`
                
                .. attribute:: explicit_route_objects
                
                	List of explicit route objects
                	**type**\: list of :py:class:`ExplicitRouteObjects <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects>`
                
                .. attribute:: state
                
                	Operational state parameters relating to the named explicit paths
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.config = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config()
                    self.config.parent = self
                    self.explicit_route_objects = YList()
                    self.explicit_route_objects.parent = self
                    self.explicit_route_objects.name = 'explicit_route_objects'
                    self.state = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to named explicit
                    paths
                    
                    .. attribute:: name
                    
                    	A string name that uniquely identifies an explicit path
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config']['meta_info']


                class ExplicitRouteObjects(object):
                    """
                    List of explicit route objects
                    
                    .. attribute:: index
                    
                    	Index of this explicit route object, to express the order of hops in path
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to an explicit route
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters relating to an explicit route
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.config = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config()
                        self.config.parent = self
                        self.state = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to an explicit
                        route
                        
                        .. attribute:: address
                        
                        	router hop for the LSP path
                        	**type**\: one of { str | str }
                        
                        .. attribute:: hop_type
                        
                        	strict or loose hop
                        	**type**\: :py:class:`MplsHopType_Enum <ydk.models.openconfig.openconfig_mpls.MplsHopType_Enum>`
                        
                        .. attribute:: index
                        
                        	Index of this explicit route object to express the order of hops in the path
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.hop_type = None
                            self.index = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.address is not None:
                                return True

                            if self.hop_type is not None:
                                return True

                            if self.index is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config']['meta_info']


                    class State(object):
                        """
                        State parameters relating to an explicit route
                        
                        .. attribute:: address
                        
                        	router hop for the LSP path
                        	**type**\: one of { str | str }
                        
                        .. attribute:: hop_type
                        
                        	strict or loose hop
                        	**type**\: :py:class:`MplsHopType_Enum <ydk.models.openconfig.openconfig_mpls.MplsHopType_Enum>`
                        
                        .. attribute:: index
                        
                        	Index of this explicit route object to express the order of hops in the path
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.hop_type = None
                            self.index = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.address is not None:
                                return True

                            if self.hop_type is not None:
                                return True

                            if self.index is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYDataValidationError('Key property index is None')

                        return self.parent._common_path +'/openconfig-mpls:explicit-route-objects[openconfig-mpls:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.index is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.config is not None and self.config.is_presence():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.state is not None and self.state.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects']['meta_info']


                class State(object):
                    """
                    Operational state parameters relating to the named
                    explicit paths
                    
                    .. attribute:: name
                    
                    	A string name that uniquely identifies an explicit path
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:constrained-path/openconfig-mpls:named-explicit-paths[openconfig-mpls:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.config is not None and self.config.is_presence():
                        return True

                    if self.explicit_route_objects is not None:
                        for child_ref in self.explicit_route_objects:
                            if child_ref._has_data():
                                return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths']['meta_info']


            class Tunnel(object):
                """
                List of TE tunnels
                
                .. attribute:: name
                
                	The tunnel name
                	**type**\: str
                
                .. attribute:: type
                
                	The tunnel type, p2p or p2mp
                	**type**\: :py:class:`TunnelType_Identity <ydk.models.openconfig.openconfig_mpls_types.TunnelType_Identity>`
                
                .. attribute:: bandwidth
                
                	Bandwidth configuration for TE LSPs
                	**type**\: :py:class:`Bandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth>`
                
                .. attribute:: config
                
                	Configuration parameters related to TE tunnels\:
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Config>`
                
                .. attribute:: p2p_tunnel_attributes
                
                	Parameters related to LSPs of type P2P
                	**type**\: :py:class:`P2pTunnelAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes>`
                
                .. attribute:: state
                
                	State parameters related to TE tunnels
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.type = None
                    self.bandwidth = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth()
                    self.bandwidth.parent = self
                    self.config = Mpls.Lsps.ConstrainedPath.Tunnel.Config()
                    self.config.parent = self
                    self.p2p_tunnel_attributes = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes()
                    self.p2p_tunnel_attributes.parent = self
                    self.state = Mpls.Lsps.ConstrainedPath.Tunnel.State()
                    self.state.parent = self


                class Bandwidth(object):
                    """
                    Bandwidth configuration for TE LSPs
                    
                    .. attribute:: auto_bandwidth
                    
                    	Parameters related to auto\-bandwidth
                    	**type**\: :py:class:`AutoBandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters related to bandwidth on TE tunnels\:
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters related to bandwidth configuration of TE tunnels
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.auto_bandwidth = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth()
                        self.auto_bandwidth.parent = self
                        self.config = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config()
                        self.config.parent = self
                        self.state = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State()
                        self.state.parent = self


                    class AutoBandwidth(object):
                        """
                        Parameters related to auto\-bandwidth
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to MPLS auto\-bandwidth on the tunnel
                        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config>`
                        
                        .. attribute:: overflow
                        
                        	configuration of MPLS overflow bandwidth adjustement for the LSP
                        	**type**\: :py:class:`Overflow <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to MPLS auto\-bandwidth on the tunnel
                        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State>`
                        
                        .. attribute:: underflow
                        
                        	configuration of MPLS underflow bandwidth           adjustement for the LSP
                        	**type**\: :py:class:`Underflow <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.config = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config()
                            self.config.parent = self
                            self.overflow = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow()
                            self.overflow.parent = self
                            self.state = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State()
                            self.state.parent = self
                            self.underflow = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow()
                            self.underflow.parent = self


                        class Config(object):
                            """
                            Configuration parameters relating to MPLS
                            auto\-bandwidth on the tunnel.
                            
                            .. attribute:: adjust_interval
                            
                            	time in seconds between adjustments to LSP bandwidth
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjust_threshold
                            
                            	percentage difference between the LSP's specified bandwidth and its current bandwidth allocation \-\- if the difference is greater than the specified percentage, auto\-bandwidth adjustment is triggered
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: enabled
                            
                            	enables mpls auto\-bandwidth on the lsp
                            	**type**\: bool
                            
                            .. attribute:: max_bw
                            
                            	set the maximum bandwidth in Mbps for an auto\-bandwidth LSP
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: min_bw
                            
                            	set the minimum bandwidth in Mbps for an auto\-bandwidth LSP
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.adjust_interval = None
                                self.adjust_threshold = None
                                self.enabled = None
                                self.max_bw = None
                                self.min_bw = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.adjust_interval is not None:
                                    return True

                                if self.adjust_threshold is not None:
                                    return True

                                if self.enabled is not None:
                                    return True

                                if self.max_bw is not None:
                                    return True

                                if self.min_bw is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config']['meta_info']


                        class Overflow(object):
                            """
                            configuration of MPLS overflow bandwidth
                            adjustement for the LSP
                            
                            .. attribute:: config
                            
                            	Config information for MPLS overflow bandwidth adjustment
                            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config>`
                            
                            .. attribute:: state
                            
                            	Config information for MPLS overflow bandwidth adjustment
                            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.config = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config()
                                self.config.parent = self
                                self.state = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State()
                                self.state.parent = self


                            class Config(object):
                                """
                                Config information for MPLS overflow bandwidth
                                adjustment
                                
                                .. attribute:: enabled
                                
                                	enables mpls lsp bandwidth overflow adjustment on the lsp
                                	**type**\: bool
                                
                                .. attribute:: overflow_threshold
                                
                                	bandwidth percentage change to trigger an overflow event
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: trigger_event_count
                                
                                	number of consecutive overflow sample events needed to trigger an overflow adjustment
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    self.parent = None
                                    self.enabled = None
                                    self.overflow_threshold = None
                                    self.trigger_event_count = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-mpls:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.enabled is not None:
                                        return True

                                    if self.overflow_threshold is not None:
                                        return True

                                    if self.trigger_event_count is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config']['meta_info']


                            class State(object):
                                """
                                Config information for MPLS overflow bandwidth
                                adjustment
                                
                                .. attribute:: enabled
                                
                                	enables mpls lsp bandwidth overflow adjustment on the lsp
                                	**type**\: bool
                                
                                .. attribute:: overflow_threshold
                                
                                	bandwidth percentage change to trigger an overflow event
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: trigger_event_count
                                
                                	number of consecutive overflow sample events needed to trigger an overflow adjustment
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    self.parent = None
                                    self.enabled = None
                                    self.overflow_threshold = None
                                    self.trigger_event_count = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-mpls:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.enabled is not None:
                                        return True

                                    if self.overflow_threshold is not None:
                                        return True

                                    if self.trigger_event_count is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:overflow'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.config is not None and self.config.is_presence():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                if self.state is not None and self.state.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow']['meta_info']


                        class State(object):
                            """
                            State parameters relating to MPLS
                            auto\-bandwidth on the tunnel.
                            
                            .. attribute:: adjust_interval
                            
                            	time in seconds between adjustments to LSP bandwidth
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjust_threshold
                            
                            	percentage difference between the LSP's specified bandwidth and its current bandwidth allocation \-\- if the difference is greater than the specified percentage, auto\-bandwidth adjustment is triggered
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: enabled
                            
                            	enables mpls auto\-bandwidth on the lsp
                            	**type**\: bool
                            
                            .. attribute:: max_bw
                            
                            	set the maximum bandwidth in Mbps for an auto\-bandwidth LSP
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: min_bw
                            
                            	set the minimum bandwidth in Mbps for an auto\-bandwidth LSP
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.adjust_interval = None
                                self.adjust_threshold = None
                                self.enabled = None
                                self.max_bw = None
                                self.min_bw = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.adjust_interval is not None:
                                    return True

                                if self.adjust_threshold is not None:
                                    return True

                                if self.enabled is not None:
                                    return True

                                if self.max_bw is not None:
                                    return True

                                if self.min_bw is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State']['meta_info']


                        class Underflow(object):
                            """
                            configuration of MPLS underflow bandwidth
                                      adjustement for the LSP
                            
                            .. attribute:: config
                            
                            	Config information for MPLS underflow bandwidth           adjustment
                            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config>`
                            
                            .. attribute:: state
                            
                            	State information for MPLS underflow bandwidth           adjustment
                            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.config = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config()
                                self.config.parent = self
                                self.state = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State()
                                self.state.parent = self


                            class Config(object):
                                """
                                Config information for MPLS underflow bandwidth
                                          adjustment
                                
                                .. attribute:: enabled
                                
                                	enables bandwidth underflow adjustment on the lsp
                                	**type**\: bool
                                
                                .. attribute:: trigger_event_count
                                
                                	number of consecutive underflow sample events needed to trigger an underflow adjustment
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: underflow_threshold
                                
                                	bandwidth percentage change to trigger and underflow event
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    self.parent = None
                                    self.enabled = None
                                    self.trigger_event_count = None
                                    self.underflow_threshold = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-mpls:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.enabled is not None:
                                        return True

                                    if self.trigger_event_count is not None:
                                        return True

                                    if self.underflow_threshold is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config']['meta_info']


                            class State(object):
                                """
                                State information for MPLS underflow bandwidth
                                          adjustment
                                
                                .. attribute:: enabled
                                
                                	enables bandwidth underflow adjustment on the lsp
                                	**type**\: bool
                                
                                .. attribute:: trigger_event_count
                                
                                	number of consecutive underflow sample events needed to trigger an underflow adjustment
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: underflow_threshold
                                
                                	bandwidth percentage change to trigger and underflow event
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    self.parent = None
                                    self.enabled = None
                                    self.trigger_event_count = None
                                    self.underflow_threshold = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-mpls:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.enabled is not None:
                                        return True

                                    if self.trigger_event_count is not None:
                                        return True

                                    if self.underflow_threshold is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:underflow'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.config is not None and self.config.is_presence():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                if self.state is not None and self.state.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:auto-bandwidth'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.config is not None and self.config.is_presence():
                                return True

                            if self.overflow is not None and self.overflow._has_data():
                                return True

                            if self.overflow is not None and self.overflow.is_presence():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.state is not None and self.state.is_presence():
                                return True

                            if self.underflow is not None and self.underflow._has_data():
                                return True

                            if self.underflow is not None and self.underflow.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth']['meta_info']


                    class Config(object):
                        """
                        Configuration parameters related to bandwidth on TE
                        tunnels\:
                        
                        .. attribute:: set_bandwidth
                        
                        	set bandwidth explicitly, e.g., using offline calculation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: specification_type
                        
                        	The method used for settign the bandwidth, either explicitly specified or configured
                        	**type**\: :py:class:`TeBandwidthType_Enum <ydk.models.openconfig.openconfig_mpls.TeBandwidthType_Enum>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.set_bandwidth = None
                            self.specification_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.set_bandwidth is not None:
                                return True

                            if self.specification_type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config']['meta_info']


                    class State(object):
                        """
                        State parameters related to bandwidth
                        configuration of TE tunnels
                        
                        .. attribute:: set_bandwidth
                        
                        	set bandwidth explicitly, e.g., using offline calculation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: specification_type
                        
                        	The method used for settign the bandwidth, either explicitly specified or configured
                        	**type**\: :py:class:`TeBandwidthType_Enum <ydk.models.openconfig.openconfig_mpls.TeBandwidthType_Enum>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.set_bandwidth = None
                            self.specification_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.set_bandwidth is not None:
                                return True

                            if self.specification_type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:bandwidth'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.auto_bandwidth is not None and self.auto_bandwidth._has_data():
                            return True

                        if self.auto_bandwidth is not None and self.auto_bandwidth.is_presence():
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.config is not None and self.config.is_presence():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.state is not None and self.state.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth']['meta_info']


                class Config(object):
                    """
                    Configuration parameters related to TE tunnels\:
                    
                    .. attribute:: admin_status
                    
                    	TE tunnel administrative state
                    	**type**\: :py:class:`TunnelAdminStatus_Identity <ydk.models.openconfig.openconfig_mpls_types.TunnelAdminStatus_Identity>`
                    
                    .. attribute:: description
                    
                    	optional text description for the tunnel
                    	**type**\: str
                    
                    .. attribute:: hold_priority
                    
                    	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: local_id
                    
                    	locally signficant optional identifier for the tunnel; may be a numerical or string value
                    	**type**\: one of { int | str }
                    
                    .. attribute:: metric
                    
                    	LSP metric, either explicit or IGP
                    	**type**\: one of { :py:class:`TeMetricType_Enum <ydk.models.openconfig.openconfig_mpls.TeMetricType_Enum>` | int }
                    
                    .. attribute:: name
                    
                    	The tunnel name
                    	**type**\: str
                    
                    .. attribute:: preference
                    
                    	Specifies a preference for this tunnel. A lower number signifies a better preference
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    .. attribute:: protection_style_requested
                    
                    	style of mpls frr protection desired\: can be link, link\-node or unprotected
                    	**type**\: :py:class:`ProtectionType_Identity <ydk.models.openconfig.openconfig_mpls_types.ProtectionType_Identity>`
                    
                    .. attribute:: reoptimize_timer
                    
                    	frequency of reoptimization of a traffic engineered LSP
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: setup_priority
                    
                    	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: signaling_protocol
                    
                    	Signaling protocol used to set up this tunnel
                    	**type**\: :py:class:`TunnelType_Identity <ydk.models.openconfig.openconfig_mpls_types.TunnelType_Identity>`
                    
                    .. attribute:: soft_preemption
                    
                    	Enables RSVP soft\-preemption on this LSP
                    	**type**\: bool
                    
                    .. attribute:: source
                    
                    	RSVP\-TE tunnel source address
                    	**type**\: one of { str | str }
                    
                    .. attribute:: type
                    
                    	Tunnel type, p2p or p2mp
                    	**type**\: :py:class:`TunnelType_Identity <ydk.models.openconfig.openconfig_mpls_types.TunnelType_Identity>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.admin_status = None
                        self.description = None
                        self.hold_priority = None
                        self.local_id = None
                        self.metric = None
                        self.name = None
                        self.preference = None
                        self.protection_style_requested = None
                        self.reoptimize_timer = None
                        self.setup_priority = None
                        self.signaling_protocol = None
                        self.soft_preemption = None
                        self.source = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.admin_status is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.hold_priority is not None:
                            return True

                        if self.local_id is not None:
                            return True

                        if self.metric is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.preference is not None:
                            return True

                        if self.protection_style_requested is not None:
                            return True

                        if self.reoptimize_timer is not None:
                            return True

                        if self.setup_priority is not None:
                            return True

                        if self.signaling_protocol is not None:
                            return True

                        if self.soft_preemption is not None:
                            return True

                        if self.source is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Config']['meta_info']


                class P2pTunnelAttributes(object):
                    """
                    Parameters related to LSPs of type P2P
                    
                    .. attribute:: config
                    
                    	Configuration parameters for P2P LSPs
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.Config>`
                    
                    .. attribute:: p2p_primary_paths
                    
                    	List of p2p primary paths for a tunnel
                    	**type**\: list of :py:class:`P2pPrimaryPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths>`
                    
                    .. attribute:: p2p_secondary_paths
                    
                    	List of p2p primary paths for a tunnel
                    	**type**\: list of :py:class:`P2pSecondaryPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths>`
                    
                    .. attribute:: state
                    
                    	State parameters for P2P LSPs
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.Config()
                        self.config.parent = self
                        self.p2p_primary_paths = YList()
                        self.p2p_primary_paths.parent = self
                        self.p2p_primary_paths.name = 'p2p_primary_paths'
                        self.p2p_secondary_paths = YList()
                        self.p2p_secondary_paths.parent = self
                        self.p2p_secondary_paths.name = 'p2p_secondary_paths'
                        self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters for P2P LSPs
                        
                        .. attribute:: destination
                        
                        	P2P tunnel destination address
                        	**type**\: one of { str | str }
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.destination = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.destination is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.Config']['meta_info']


                    class P2pPrimaryPaths(object):
                        """
                        List of p2p primary paths for a tunnel
                        
                        .. attribute:: name
                        
                        	Path name
                        	**type**\: str
                        
                        .. attribute:: admin_groups
                        
                        	Top\-level container for include/exclude constraints for link affinities
                        	**type**\: :py:class:`AdminGroups <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.AdminGroups>`
                        
                        .. attribute:: candidate_secondary_paths
                        
                        	The set of candidate secondary paths which may be used for this primary path. When secondary paths are specified in the list the path of the secondary LSP in use must be restricted to those path options referenced. The priority of the secondary paths is specified within the list. Higher priority values are less preferred \- that is to say that a path with priority 0 is the most preferred path. In the case that the list is empty, any secondary path option may be utilised when the current primary path is in use
                        	**type**\: :py:class:`CandidateSecondaryPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to paths
                        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters related to paths
                        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.admin_groups = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.AdminGroups()
                            self.admin_groups.parent = self
                            self.candidate_secondary_paths = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths()
                            self.candidate_secondary_paths.parent = self
                            self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.Config()
                            self.config.parent = self
                            self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.State()
                            self.state.parent = self


                        class AdminGroups(object):
                            """
                            Top\-level container for include/exclude constraints for
                            link affinities
                            
                            .. attribute:: config
                            
                            	Configuration data 
                            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.AdminGroups.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data 
                            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.AdminGroups.State>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.AdminGroups.Config()
                                self.config.parent = self
                                self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.AdminGroups.State()
                                self.state.parent = self


                            class Config(object):
                                """
                                Configuration data 
                                
                                .. attribute:: exclude_group
                                
                                	list of references to named admin\-groups to exclude in path calculation
                                	**type**\: list of str
                                
                                .. attribute:: include_all_group
                                
                                	list of references to named admin\-groups of which all must be included
                                	**type**\: list of str
                                
                                .. attribute:: include_any_group
                                
                                	list of references to named admin\-groups of which one must be included
                                	**type**\: list of str
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    self.parent = None
                                    self.exclude_group = []
                                    self.include_all_group = []
                                    self.include_any_group = []

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-mpls:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.exclude_group is not None:
                                        for child in self.exclude_group:
                                            if child is not None:
                                                return True

                                    if self.include_all_group is not None:
                                        for child in self.include_all_group:
                                            if child is not None:
                                                return True

                                    if self.include_any_group is not None:
                                        for child in self.include_any_group:
                                            if child is not None:
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.AdminGroups.Config']['meta_info']


                            class State(object):
                                """
                                Operational state data 
                                
                                .. attribute:: exclude_group
                                
                                	list of references to named admin\-groups to exclude in path calculation
                                	**type**\: list of str
                                
                                .. attribute:: include_all_group
                                
                                	list of references to named admin\-groups of which all must be included
                                	**type**\: list of str
                                
                                .. attribute:: include_any_group
                                
                                	list of references to named admin\-groups of which one must be included
                                	**type**\: list of str
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    self.parent = None
                                    self.exclude_group = []
                                    self.include_all_group = []
                                    self.include_any_group = []

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-mpls:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.exclude_group is not None:
                                        for child in self.exclude_group:
                                            if child is not None:
                                                return True

                                    if self.include_all_group is not None:
                                        for child in self.include_all_group:
                                            if child is not None:
                                                return True

                                    if self.include_any_group is not None:
                                        for child in self.include_any_group:
                                            if child is not None:
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.AdminGroups.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:admin-groups'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.config is not None and self.config.is_presence():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                if self.state is not None and self.state.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.AdminGroups']['meta_info']


                        class CandidateSecondaryPaths(object):
                            """
                            The set of candidate secondary paths which may be used
                            for this primary path. When secondary paths are specified
                            in the list the path of the secondary LSP in use must be
                            restricted to those path options referenced. The
                            priority of the secondary paths is specified within the
                            list. Higher priority values are less preferred \- that is
                            to say that a path with priority 0 is the most preferred
                            path. In the case that the list is empty, any secondary
                            path option may be utilised when the current primary path
                            is in use.
                            
                            .. attribute:: candidate_secondary_path
                            
                            	List of secondary paths which may be utilised when the current primary path is in use
                            	**type**\: list of :py:class:`CandidateSecondaryPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.candidate_secondary_path = YList()
                                self.candidate_secondary_path.parent = self
                                self.candidate_secondary_path.name = 'candidate_secondary_path'


                            class CandidateSecondaryPath(object):
                                """
                                List of secondary paths which may be utilised when the
                                current primary path is in use
                                
                                .. attribute:: secondary_path
                                
                                	A reference to the secondary path option reference which acts as the key of the candidate\-secondary\-path list
                                	**type**\: str
                                
                                .. attribute:: config
                                
                                	Configuration parameters relating to the candidate secondary path
                                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state parameters relating to the candidate secondary path
                                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State>`
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    self.parent = None
                                    self.secondary_path = None
                                    self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config()
                                    self.config.parent = self
                                    self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State()
                                    self.state.parent = self


                                class Config(object):
                                    """
                                    Configuration parameters relating to the candidate
                                    secondary path
                                    
                                    .. attribute:: priority
                                    
                                    	The priority of the specified secondary path option. Higher priority options are less preferable \- such that a secondary path reference with a priority of 0 is the most preferred
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: secondary_path
                                    
                                    	A reference to the secondary path that should be utilised when the containing primary path option is in use
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'mpls'
                                    _revision = '2015-11-05'

                                    def __init__(self):
                                        self.parent = None
                                        self.priority = None
                                        self.secondary_path = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-mpls:config'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.priority is not None:
                                            return True

                                        if self.secondary_path is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                        return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config']['meta_info']


                                class State(object):
                                    """
                                    Operational state parameters relating to the candidate
                                    secondary path
                                    
                                    .. attribute:: active
                                    
                                    	Indicates the current active path option that has been selected of the candidate secondary paths
                                    	**type**\: bool
                                    
                                    .. attribute:: priority
                                    
                                    	The priority of the specified secondary path option. Higher priority options are less preferable \- such that a secondary path reference with a priority of 0 is the most preferred
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: secondary_path
                                    
                                    	A reference to the secondary path that should be utilised when the containing primary path option is in use
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'mpls'
                                    _revision = '2015-11-05'

                                    def __init__(self):
                                        self.parent = None
                                        self.active = None
                                        self.priority = None
                                        self.secondary_path = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-mpls:state'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.active is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        if self.secondary_path is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                        return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.secondary_path is None:
                                        raise YPYDataValidationError('Key property secondary_path is None')

                                    return self.parent._common_path +'/openconfig-mpls:candidate-secondary-path[openconfig-mpls:secondary-path = ' + str(self.secondary_path) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.secondary_path is not None:
                                        return True

                                    if self.config is not None and self.config._has_data():
                                        return True

                                    if self.config is not None and self.config.is_presence():
                                        return True

                                    if self.state is not None and self.state._has_data():
                                        return True

                                    if self.state is not None and self.state.is_presence():
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:candidate-secondary-paths'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.candidate_secondary_path is not None:
                                    for child_ref in self.candidate_secondary_path:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.CandidateSecondaryPaths']['meta_info']


                        class Config(object):
                            """
                            Configuration parameters related to paths
                            
                            .. attribute:: cspf_tiebreaker
                            
                            	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                            	**type**\: :py:class:`CspfTieBreaking_Enum <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking_Enum>`
                            
                            .. attribute:: explicit_path_name
                            
                            	reference to a defined path
                            	**type**\: str
                            
                            .. attribute:: hold_priority
                            
                            	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: name
                            
                            	Path name
                            	**type**\: str
                            
                            .. attribute:: path_computation_method
                            
                            	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                            	**type**\: :py:class:`PathComputationMethod_Identity <ydk.models.openconfig.openconfig_mpls.PathComputationMethod_Identity>`
                            
                            .. attribute:: path_computation_server
                            
                            	Address of the external path computation server
                            	**type**\: one of { str | str }
                            
                            .. attribute:: preference
                            
                            	Specifies a preference for this path. The lower the number higher the preference
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            .. attribute:: retry_timer
                            
                            	sets the time between attempts to establish the LSP
                            	**type**\: int
                            
                            	**range:** 1..600
                            
                            .. attribute:: setup_priority
                            
                            	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: use_cspf
                            
                            	Flag to enable CSPF for locally computed LSPs
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.cspf_tiebreaker = None
                                self.explicit_path_name = None
                                self.hold_priority = None
                                self.name = None
                                self.path_computation_method = None
                                self.path_computation_server = None
                                self.preference = None
                                self.retry_timer = None
                                self.setup_priority = None
                                self.use_cspf = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.cspf_tiebreaker is not None:
                                    return True

                                if self.explicit_path_name is not None:
                                    return True

                                if self.hold_priority is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                if self.path_computation_method is not None:
                                    return True

                                if self.path_computation_server is not None:
                                    return True

                                if self.preference is not None:
                                    return True

                                if self.retry_timer is not None:
                                    return True

                                if self.setup_priority is not None:
                                    return True

                                if self.use_cspf is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.Config']['meta_info']


                        class State(object):
                            """
                            State parameters related to paths
                            
                            .. attribute:: cspf_tiebreaker
                            
                            	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                            	**type**\: :py:class:`CspfTieBreaking_Enum <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking_Enum>`
                            
                            .. attribute:: explicit_path_name
                            
                            	reference to a defined path
                            	**type**\: str
                            
                            .. attribute:: hold_priority
                            
                            	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: name
                            
                            	Path name
                            	**type**\: str
                            
                            .. attribute:: path_computation_method
                            
                            	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                            	**type**\: :py:class:`PathComputationMethod_Identity <ydk.models.openconfig.openconfig_mpls.PathComputationMethod_Identity>`
                            
                            .. attribute:: path_computation_server
                            
                            	Address of the external path computation server
                            	**type**\: one of { str | str }
                            
                            .. attribute:: preference
                            
                            	Specifies a preference for this path. The lower the number higher the preference
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            .. attribute:: retry_timer
                            
                            	sets the time between attempts to establish the LSP
                            	**type**\: int
                            
                            	**range:** 1..600
                            
                            .. attribute:: setup_priority
                            
                            	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: use_cspf
                            
                            	Flag to enable CSPF for locally computed LSPs
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.cspf_tiebreaker = None
                                self.explicit_path_name = None
                                self.hold_priority = None
                                self.name = None
                                self.path_computation_method = None
                                self.path_computation_server = None
                                self.preference = None
                                self.retry_timer = None
                                self.setup_priority = None
                                self.use_cspf = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.cspf_tiebreaker is not None:
                                    return True

                                if self.explicit_path_name is not None:
                                    return True

                                if self.hold_priority is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                if self.path_computation_method is not None:
                                    return True

                                if self.path_computation_server is not None:
                                    return True

                                if self.preference is not None:
                                    return True

                                if self.retry_timer is not None:
                                    return True

                                if self.setup_priority is not None:
                                    return True

                                if self.use_cspf is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYDataValidationError('Key property name is None')

                            return self.parent._common_path +'/openconfig-mpls:p2p-primary-paths[openconfig-mpls:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.name is not None:
                                return True

                            if self.admin_groups is not None and self.admin_groups._has_data():
                                return True

                            if self.admin_groups is not None and self.admin_groups.is_presence():
                                return True

                            if self.candidate_secondary_paths is not None and self.candidate_secondary_paths._has_data():
                                return True

                            if self.candidate_secondary_paths is not None and self.candidate_secondary_paths.is_presence():
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.config is not None and self.config.is_presence():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.state is not None and self.state.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pPrimaryPaths']['meta_info']


                    class P2pSecondaryPaths(object):
                        """
                        List of p2p primary paths for a tunnel
                        
                        .. attribute:: name
                        
                        	Path name
                        	**type**\: str
                        
                        .. attribute:: admin_groups
                        
                        	Top\-level container for include/exclude constraints for link affinities
                        	**type**\: :py:class:`AdminGroups <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.AdminGroups>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to paths
                        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters related to paths
                        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.admin_groups = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.AdminGroups()
                            self.admin_groups.parent = self
                            self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.Config()
                            self.config.parent = self
                            self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.State()
                            self.state.parent = self


                        class AdminGroups(object):
                            """
                            Top\-level container for include/exclude constraints for
                            link affinities
                            
                            .. attribute:: config
                            
                            	Configuration data 
                            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.AdminGroups.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data 
                            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.AdminGroups.State>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.AdminGroups.Config()
                                self.config.parent = self
                                self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.AdminGroups.State()
                                self.state.parent = self


                            class Config(object):
                                """
                                Configuration data 
                                
                                .. attribute:: exclude_group
                                
                                	list of references to named admin\-groups to exclude in path calculation
                                	**type**\: list of str
                                
                                .. attribute:: include_all_group
                                
                                	list of references to named admin\-groups of which all must be included
                                	**type**\: list of str
                                
                                .. attribute:: include_any_group
                                
                                	list of references to named admin\-groups of which one must be included
                                	**type**\: list of str
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    self.parent = None
                                    self.exclude_group = []
                                    self.include_all_group = []
                                    self.include_any_group = []

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-mpls:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.exclude_group is not None:
                                        for child in self.exclude_group:
                                            if child is not None:
                                                return True

                                    if self.include_all_group is not None:
                                        for child in self.include_all_group:
                                            if child is not None:
                                                return True

                                    if self.include_any_group is not None:
                                        for child in self.include_any_group:
                                            if child is not None:
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.AdminGroups.Config']['meta_info']


                            class State(object):
                                """
                                Operational state data 
                                
                                .. attribute:: exclude_group
                                
                                	list of references to named admin\-groups to exclude in path calculation
                                	**type**\: list of str
                                
                                .. attribute:: include_all_group
                                
                                	list of references to named admin\-groups of which all must be included
                                	**type**\: list of str
                                
                                .. attribute:: include_any_group
                                
                                	list of references to named admin\-groups of which one must be included
                                	**type**\: list of str
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    self.parent = None
                                    self.exclude_group = []
                                    self.include_all_group = []
                                    self.include_any_group = []

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-mpls:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.exclude_group is not None:
                                        for child in self.exclude_group:
                                            if child is not None:
                                                return True

                                    if self.include_all_group is not None:
                                        for child in self.include_all_group:
                                            if child is not None:
                                                return True

                                    if self.include_any_group is not None:
                                        for child in self.include_any_group:
                                            if child is not None:
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.AdminGroups.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:admin-groups'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.config is not None and self.config.is_presence():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                if self.state is not None and self.state.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.AdminGroups']['meta_info']


                        class Config(object):
                            """
                            Configuration parameters related to paths
                            
                            .. attribute:: cspf_tiebreaker
                            
                            	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                            	**type**\: :py:class:`CspfTieBreaking_Enum <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking_Enum>`
                            
                            .. attribute:: explicit_path_name
                            
                            	reference to a defined path
                            	**type**\: str
                            
                            .. attribute:: hold_priority
                            
                            	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: name
                            
                            	Path name
                            	**type**\: str
                            
                            .. attribute:: path_computation_method
                            
                            	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                            	**type**\: :py:class:`PathComputationMethod_Identity <ydk.models.openconfig.openconfig_mpls.PathComputationMethod_Identity>`
                            
                            .. attribute:: path_computation_server
                            
                            	Address of the external path computation server
                            	**type**\: one of { str | str }
                            
                            .. attribute:: preference
                            
                            	Specifies a preference for this path. The lower the number higher the preference
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            .. attribute:: retry_timer
                            
                            	sets the time between attempts to establish the LSP
                            	**type**\: int
                            
                            	**range:** 1..600
                            
                            .. attribute:: setup_priority
                            
                            	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: use_cspf
                            
                            	Flag to enable CSPF for locally computed LSPs
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.cspf_tiebreaker = None
                                self.explicit_path_name = None
                                self.hold_priority = None
                                self.name = None
                                self.path_computation_method = None
                                self.path_computation_server = None
                                self.preference = None
                                self.retry_timer = None
                                self.setup_priority = None
                                self.use_cspf = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.cspf_tiebreaker is not None:
                                    return True

                                if self.explicit_path_name is not None:
                                    return True

                                if self.hold_priority is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                if self.path_computation_method is not None:
                                    return True

                                if self.path_computation_server is not None:
                                    return True

                                if self.preference is not None:
                                    return True

                                if self.retry_timer is not None:
                                    return True

                                if self.setup_priority is not None:
                                    return True

                                if self.use_cspf is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.Config']['meta_info']


                        class State(object):
                            """
                            State parameters related to paths
                            
                            .. attribute:: cspf_tiebreaker
                            
                            	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                            	**type**\: :py:class:`CspfTieBreaking_Enum <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking_Enum>`
                            
                            .. attribute:: explicit_path_name
                            
                            	reference to a defined path
                            	**type**\: str
                            
                            .. attribute:: hold_priority
                            
                            	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: name
                            
                            	Path name
                            	**type**\: str
                            
                            .. attribute:: path_computation_method
                            
                            	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                            	**type**\: :py:class:`PathComputationMethod_Identity <ydk.models.openconfig.openconfig_mpls.PathComputationMethod_Identity>`
                            
                            .. attribute:: path_computation_server
                            
                            	Address of the external path computation server
                            	**type**\: one of { str | str }
                            
                            .. attribute:: preference
                            
                            	Specifies a preference for this path. The lower the number higher the preference
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            .. attribute:: retry_timer
                            
                            	sets the time between attempts to establish the LSP
                            	**type**\: int
                            
                            	**range:** 1..600
                            
                            .. attribute:: setup_priority
                            
                            	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: use_cspf
                            
                            	Flag to enable CSPF for locally computed LSPs
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.cspf_tiebreaker = None
                                self.explicit_path_name = None
                                self.hold_priority = None
                                self.name = None
                                self.path_computation_method = None
                                self.path_computation_server = None
                                self.preference = None
                                self.retry_timer = None
                                self.setup_priority = None
                                self.use_cspf = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.cspf_tiebreaker is not None:
                                    return True

                                if self.explicit_path_name is not None:
                                    return True

                                if self.hold_priority is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                if self.path_computation_method is not None:
                                    return True

                                if self.path_computation_server is not None:
                                    return True

                                if self.preference is not None:
                                    return True

                                if self.retry_timer is not None:
                                    return True

                                if self.setup_priority is not None:
                                    return True

                                if self.use_cspf is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYDataValidationError('Key property name is None')

                            return self.parent._common_path +'/openconfig-mpls:p2p-secondary-paths[openconfig-mpls:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.name is not None:
                                return True

                            if self.admin_groups is not None and self.admin_groups._has_data():
                                return True

                            if self.admin_groups is not None and self.admin_groups.is_presence():
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.config is not None and self.config.is_presence():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.state is not None and self.state.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths']['meta_info']


                    class State(object):
                        """
                        State parameters for P2P LSPs
                        
                        .. attribute:: destination
                        
                        	P2P tunnel destination address
                        	**type**\: one of { str | str }
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.destination = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.destination is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:p2p-tunnel-attributes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.config is not None and self.config.is_presence():
                            return True

                        if self.p2p_primary_paths is not None:
                            for child_ref in self.p2p_primary_paths:
                                if child_ref._has_data():
                                    return True

                        if self.p2p_secondary_paths is not None:
                            for child_ref in self.p2p_secondary_paths:
                                if child_ref._has_data():
                                    return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.state is not None and self.state.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2pTunnelAttributes']['meta_info']


                class State(object):
                    """
                    State parameters related to TE tunnels
                    
                    .. attribute:: admin_status
                    
                    	TE tunnel administrative state
                    	**type**\: :py:class:`TunnelAdminStatus_Identity <ydk.models.openconfig.openconfig_mpls_types.TunnelAdminStatus_Identity>`
                    
                    .. attribute:: counters
                    
                    	State data for MPLS label switched paths. This state data is specific to a single label switched path
                    	**type**\: :py:class:`Counters <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters>`
                    
                    .. attribute:: description
                    
                    	optional text description for the tunnel
                    	**type**\: str
                    
                    .. attribute:: hold_priority
                    
                    	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: local_id
                    
                    	locally signficant optional identifier for the tunnel; may be a numerical or string value
                    	**type**\: one of { int | str }
                    
                    .. attribute:: metric
                    
                    	LSP metric, either explicit or IGP
                    	**type**\: one of { :py:class:`TeMetricType_Enum <ydk.models.openconfig.openconfig_mpls.TeMetricType_Enum>` | int }
                    
                    .. attribute:: name
                    
                    	The tunnel name
                    	**type**\: str
                    
                    .. attribute:: oper_status
                    
                    	The operational status of the TE tunnel
                    	**type**\: :py:class:`LspOperStatus_Identity <ydk.models.openconfig.openconfig_mpls_types.LspOperStatus_Identity>`
                    
                    .. attribute:: preference
                    
                    	Specifies a preference for this tunnel. A lower number signifies a better preference
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    .. attribute:: protection_style_requested
                    
                    	style of mpls frr protection desired\: can be link, link\-node or unprotected
                    	**type**\: :py:class:`ProtectionType_Identity <ydk.models.openconfig.openconfig_mpls_types.ProtectionType_Identity>`
                    
                    .. attribute:: reoptimize_timer
                    
                    	frequency of reoptimization of a traffic engineered LSP
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: role
                    
                    	The lsp role at the current node, whether it is headend, transit or tailend
                    	**type**\: :py:class:`LspRole_Identity <ydk.models.openconfig.openconfig_mpls_types.LspRole_Identity>`
                    
                    .. attribute:: setup_priority
                    
                    	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: signaling_protocol
                    
                    	Signaling protocol used to set up this tunnel
                    	**type**\: :py:class:`TunnelType_Identity <ydk.models.openconfig.openconfig_mpls_types.TunnelType_Identity>`
                    
                    .. attribute:: soft_preemption
                    
                    	Enables RSVP soft\-preemption on this LSP
                    	**type**\: bool
                    
                    .. attribute:: source
                    
                    	RSVP\-TE tunnel source address
                    	**type**\: one of { str | str }
                    
                    .. attribute:: type
                    
                    	Tunnel type, p2p or p2mp
                    	**type**\: :py:class:`TunnelType_Identity <ydk.models.openconfig.openconfig_mpls_types.TunnelType_Identity>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.admin_status = None
                        self.counters = Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters()
                        self.counters.parent = self
                        self.description = None
                        self.hold_priority = None
                        self.local_id = None
                        self.metric = None
                        self.name = None
                        self.oper_status = None
                        self.preference = None
                        self.protection_style_requested = None
                        self.reoptimize_timer = None
                        self.role = None
                        self.setup_priority = None
                        self.signaling_protocol = None
                        self.soft_preemption = None
                        self.source = None
                        self.type = None


                    class Counters(object):
                        """
                        State data for MPLS label switched paths. This state
                        data is specific to a single label switched path.
                        
                        .. attribute:: bytes
                        
                        	Number of bytes that have been forwarded over the label switched path
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: current_path_time
                        
                        	Indicates the time the LSP switched onto its current path. This is reset upon a LSP path change
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: next_reoptimization_time
                        
                        	Indicates the next scheduled time the LSP will be reoptimized
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: online_time
                        
                        	Indication of the time the label switched path transitioned to an Oper Up or in\-service state
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: packets
                        
                        	Number of pacets that have been forwarded over the label switched path
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: path_changes
                        
                        	Number of path changes for the label switched path
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: state_changes
                        
                        	Number of state changes for the label switched path
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.bytes = None
                            self.current_path_time = None
                            self.next_reoptimization_time = None
                            self.online_time = None
                            self.packets = None
                            self.path_changes = None
                            self.state_changes = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:counters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.bytes is not None:
                                return True

                            if self.current_path_time is not None:
                                return True

                            if self.next_reoptimization_time is not None:
                                return True

                            if self.online_time is not None:
                                return True

                            if self.packets is not None:
                                return True

                            if self.path_changes is not None:
                                return True

                            if self.state_changes is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.admin_status is not None:
                            return True

                        if self.counters is not None and self.counters._has_data():
                            return True

                        if self.counters is not None and self.counters.is_presence():
                            return True

                        if self.description is not None:
                            return True

                        if self.hold_priority is not None:
                            return True

                        if self.local_id is not None:
                            return True

                        if self.metric is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.oper_status is not None:
                            return True

                        if self.preference is not None:
                            return True

                        if self.protection_style_requested is not None:
                            return True

                        if self.reoptimize_timer is not None:
                            return True

                        if self.role is not None:
                            return True

                        if self.setup_priority is not None:
                            return True

                        if self.signaling_protocol is not None:
                            return True

                        if self.soft_preemption is not None:
                            return True

                        if self.source is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.State']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')
                    if self.type is None:
                        raise YPYDataValidationError('Key property type is None')

                    return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:constrained-path/openconfig-mpls:tunnel[openconfig-mpls:name = ' + str(self.name) + '][openconfig-mpls:type = ' + str(self.type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.type is not None:
                        return True

                    if self.bandwidth is not None and self.bandwidth._has_data():
                        return True

                    if self.bandwidth is not None and self.bandwidth.is_presence():
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.config is not None and self.config.is_presence():
                        return True

                    if self.p2p_tunnel_attributes is not None and self.p2p_tunnel_attributes._has_data():
                        return True

                    if self.p2p_tunnel_attributes is not None and self.p2p_tunnel_attributes.is_presence():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.Lsps.ConstrainedPath.Tunnel']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:constrained-path'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.named_explicit_paths is not None:
                    for child_ref in self.named_explicit_paths:
                        if child_ref._has_data():
                            return True

                if self.tunnel is not None:
                    for child_ref in self.tunnel:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.Lsps.ConstrainedPath']['meta_info']


        class StaticLsps(object):
            """
            statically configured LSPs, without dynamic
            signaling
            
            .. attribute:: label_switched_path
            
            	list of defined static LSPs
            	**type**\: list of :py:class:`LabelSwitchedPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.LabelSwitchedPath>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.label_switched_path = YList()
                self.label_switched_path.parent = self
                self.label_switched_path.name = 'label_switched_path'


            class LabelSwitchedPath(object):
                """
                list of defined static LSPs
                
                .. attribute:: name
                
                	name to identify the LSP
                	**type**\: str
                
                .. attribute:: egress
                
                	static LSPs for which the router is a egress  node
                	**type**\: :py:class:`Egress <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress>`
                
                .. attribute:: ingress
                
                	Static LSPs for which the router is an ingress node
                	**type**\: :py:class:`Ingress <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress>`
                
                .. attribute:: transit
                
                	static LSPs for which the router is a transit node
                	**type**\: :py:class:`Transit <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.egress = Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress()
                    self.egress.parent = self
                    self.ingress = Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress()
                    self.ingress.parent = self
                    self.transit = Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit()
                    self.transit.parent = self


                class Egress(object):
                    """
                    static LSPs for which the router is a
                    egress  node
                    
                    .. attribute:: incoming_label
                    
                    	label value on the incoming packet
                    	**type**\: one of { int | :py:class:`MplsLabel_Enum <ydk.models.openconfig.openconfig_mpls_types.MplsLabel_Enum>` }
                    
                    .. attribute:: next_hop
                    
                    	next hop IP address for the LSP
                    	**type**\: one of { str | str }
                    
                    .. attribute:: push_label
                    
                    	label value to push at the current hop for the LSP
                    	**type**\: one of { int | :py:class:`MplsLabel_Enum <ydk.models.openconfig.openconfig_mpls_types.MplsLabel_Enum>` }
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.incoming_label = None
                        self.next_hop = None
                        self.push_label = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:egress'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.incoming_label is not None:
                            return True

                        if self.next_hop is not None:
                            return True

                        if self.push_label is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress']['meta_info']


                class Ingress(object):
                    """
                    Static LSPs for which the router is an
                    ingress node
                    
                    .. attribute:: incoming_label
                    
                    	label value on the incoming packet
                    	**type**\: one of { int | :py:class:`MplsLabel_Enum <ydk.models.openconfig.openconfig_mpls_types.MplsLabel_Enum>` }
                    
                    .. attribute:: next_hop
                    
                    	next hop IP address for the LSP
                    	**type**\: one of { str | str }
                    
                    .. attribute:: push_label
                    
                    	label value to push at the current hop for the LSP
                    	**type**\: one of { int | :py:class:`MplsLabel_Enum <ydk.models.openconfig.openconfig_mpls_types.MplsLabel_Enum>` }
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.incoming_label = None
                        self.next_hop = None
                        self.push_label = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:ingress'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.incoming_label is not None:
                            return True

                        if self.next_hop is not None:
                            return True

                        if self.push_label is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress']['meta_info']


                class Transit(object):
                    """
                    static LSPs for which the router is a
                    transit node
                    
                    .. attribute:: incoming_label
                    
                    	label value on the incoming packet
                    	**type**\: one of { int | :py:class:`MplsLabel_Enum <ydk.models.openconfig.openconfig_mpls_types.MplsLabel_Enum>` }
                    
                    .. attribute:: next_hop
                    
                    	next hop IP address for the LSP
                    	**type**\: one of { str | str }
                    
                    .. attribute:: push_label
                    
                    	label value to push at the current hop for the LSP
                    	**type**\: one of { int | :py:class:`MplsLabel_Enum <ydk.models.openconfig.openconfig_mpls_types.MplsLabel_Enum>` }
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.incoming_label = None
                        self.next_hop = None
                        self.push_label = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:transit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.incoming_label is not None:
                            return True

                        if self.next_hop is not None:
                            return True

                        if self.push_label is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:static-lsps/openconfig-mpls:label-switched-path[openconfig-mpls:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.egress is not None and self.egress._has_data():
                        return True

                    if self.egress is not None and self.egress.is_presence():
                        return True

                    if self.ingress is not None and self.ingress._has_data():
                        return True

                    if self.ingress is not None and self.ingress.is_presence():
                        return True

                    if self.transit is not None and self.transit._has_data():
                        return True

                    if self.transit is not None and self.transit.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:static-lsps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.label_switched_path is not None:
                    for child_ref in self.label_switched_path:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.Lsps.StaticLsps']['meta_info']


        class UnconstrainedPath(object):
            """
            LSPs that use the IGP\-determined path, i.e., non
            traffic\-engineered, or non constrained\-path
            
            .. attribute:: path_setup_protocol
            
            	select and configure the signaling method for  the LSP
            	**type**\: :py:class:`PathSetupProtocol <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.path_setup_protocol = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol()
                self.path_setup_protocol.parent = self


            class PathSetupProtocol(object):
                """
                select and configure the signaling method for
                 the LSP
                
                .. attribute:: ldp
                
                	LDP signaling setup for IGP\-congruent LSPs
                	**type**\: :py:class:`Ldp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp>`
                
                .. attribute:: segment_routing
                
                	segment routing signaling extensions for IGP\-confgruent LSPs
                	**type**\: :py:class:`SegmentRouting <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.ldp = None
                    self.segment_routing = None


                class Ldp(object):
                    """
                    LDP signaling setup for IGP\-congruent LSPs
                    
                    .. attribute:: tunnel
                    
                    	contains configuration stanzas for different LSP tunnel types (P2P, P2MP, etc.)
                    	**type**\: :py:class:`Tunnel <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.tunnel = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel()
                        self.tunnel.parent = self


                    class Tunnel(object):
                        """
                        contains configuration stanzas for different LSP
                        tunnel types (P2P, P2MP, etc.)
                        
                        .. attribute:: ldp_type
                        
                        	specify basic or targeted LDP LSP
                        	**type**\: :py:class:`LdpType_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.LdpType_Enum>`
                        
                        .. attribute:: mp2mp_lsp
                        
                        	properties of multipoint\-to\-multipoint tunnels
                        	**type**\: :py:class:`Mp2mpLsp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2mpLsp>`
                        
                        .. attribute:: p2mp_lsp
                        
                        	properties of point\-to\-multipoint tunnels
                        	**type**\: :py:class:`P2mpLsp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2mpLsp>`
                        
                        .. attribute:: p2p_lsp
                        
                        	properties of point\-to\-point tunnels
                        	**type**\: :py:class:`P2pLsp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2pLsp>`
                        
                        .. attribute:: tunnel_type
                        
                        	specifies the type of LSP, e.g., P2P or P2MP
                        	**type**\: :py:class:`TunnelType_Enum <ydk.models.openconfig.openconfig_mpls_types.TunnelType_Enum>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.ldp_type = None
                            self.mp2mp_lsp = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2mpLsp()
                            self.mp2mp_lsp.parent = self
                            self.p2mp_lsp = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2mpLsp()
                            self.p2mp_lsp.parent = self
                            self.p2p_lsp = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2pLsp()
                            self.p2p_lsp.parent = self
                            self.tunnel_type = None

                        class LdpType_Enum(Enum):
                            """
                            LdpType_Enum

                            specify basic or targeted LDP LSP

                            """

                            """

                            basic hop\-by\-hop LSP

                            """
                            BASIC = 0

                            """

                            tLDP LSP

                            """
                            TARGETED = 1


                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.LdpType_Enum']



                        class Mp2mpLsp(object):
                            """
                            properties of multipoint\-to\-multipoint tunnels
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                pass

                            @property
                            def _common_path(self):

                                return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path/openconfig-mpls:path-setup-protocol/openconfig-mpls:ldp/openconfig-mpls:tunnel/openconfig-mpls:mp2mp-lsp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2mpLsp']['meta_info']


                        class P2mpLsp(object):
                            """
                            properties of point\-to\-multipoint tunnels
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                pass

                            @property
                            def _common_path(self):

                                return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path/openconfig-mpls:path-setup-protocol/openconfig-mpls:ldp/openconfig-mpls:tunnel/openconfig-mpls:p2mp-lsp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2mpLsp']['meta_info']


                        class P2pLsp(object):
                            """
                            properties of point\-to\-point tunnels
                            
                            .. attribute:: fec_address
                            
                            	Address prefix for packets sharing the same forwarding equivalence class for the IGP\-based LSP
                            	**type**\: list of one of { list of str | list of str }
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.fec_address = []

                            @property
                            def _common_path(self):

                                return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path/openconfig-mpls:path-setup-protocol/openconfig-mpls:ldp/openconfig-mpls:tunnel/openconfig-mpls:p2p-lsp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.fec_address is not None:
                                    for child in self.fec_address:
                                        if child is not None:
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2pLsp']['meta_info']

                        @property
                        def _common_path(self):

                            return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path/openconfig-mpls:path-setup-protocol/openconfig-mpls:ldp/openconfig-mpls:tunnel'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.ldp_type is not None:
                                return True

                            if self.mp2mp_lsp is not None and self.mp2mp_lsp._has_data():
                                return True

                            if self.mp2mp_lsp is not None and self.mp2mp_lsp.is_presence():
                                return True

                            if self.p2mp_lsp is not None and self.p2mp_lsp._has_data():
                                return True

                            if self.p2mp_lsp is not None and self.p2mp_lsp.is_presence():
                                return True

                            if self.p2p_lsp is not None and self.p2p_lsp._has_data():
                                return True

                            if self.p2p_lsp is not None and self.p2p_lsp.is_presence():
                                return True

                            if self.tunnel_type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel']['meta_info']

                    @property
                    def _common_path(self):

                        return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path/openconfig-mpls:path-setup-protocol/openconfig-mpls:ldp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.tunnel is not None and self.tunnel._has_data():
                            return True

                        if self.tunnel is not None and self.tunnel.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return True

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp']['meta_info']


                class SegmentRouting(object):
                    """
                    segment routing signaling extensions for
                    IGP\-confgruent LSPs
                    
                    .. attribute:: tunnel
                    
                    	contains configuration stanzas for different LSP tunnel types (P2P, P2MP, etc.)
                    	**type**\: :py:class:`Tunnel <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.tunnel = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel()
                        self.tunnel.parent = self


                    class Tunnel(object):
                        """
                        contains configuration stanzas for different LSP
                        tunnel types (P2P, P2MP, etc.)
                        
                        .. attribute:: p2p_lsp
                        
                        	properties of point\-to\-point tunnels
                        	**type**\: :py:class:`P2pLsp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp>`
                        
                        .. attribute:: tunnel_type
                        
                        	specifies the type of LSP, e.g., P2P or P2MP
                        	**type**\: :py:class:`TunnelType_Enum <ydk.models.openconfig.openconfig_mpls_types.TunnelType_Enum>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.p2p_lsp = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp()
                            self.p2p_lsp.parent = self
                            self.tunnel_type = None


                        class P2pLsp(object):
                            """
                            properties of point\-to\-point tunnels
                            
                            .. attribute:: fec
                            
                            	List of FECs that are to be originated as SR LSPs
                            	**type**\: list of :py:class:`Fec <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.fec = YList()
                                self.fec.parent = self
                                self.fec.name = 'fec'


                            class Fec(object):
                                """
                                List of FECs that are to be originated as SR LSPs
                                
                                .. attribute:: fec_address
                                
                                	FEC that is to be advertised as part of the Prefix\-SID
                                	**type**\: one of { str | str }
                                
                                .. attribute:: config
                                
                                	Configuration parameters relating to the FEC to be advertised by SR
                                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.Config>`
                                
                                .. attribute:: prefix_sid
                                
                                	Parameters relating to the Prefix\-SID used for the originated FEC
                                	**type**\: :py:class:`PrefixSid <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid>`
                                
                                .. attribute:: state
                                
                                	Operational state relating to a FEC advertised by SR
                                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.State>`
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    self.parent = None
                                    self.fec_address = None
                                    self.config = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.Config()
                                    self.config.parent = self
                                    self.prefix_sid = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid()
                                    self.prefix_sid.parent = self
                                    self.state = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.State()
                                    self.state.parent = self


                                class Config(object):
                                    """
                                    Configuration parameters relating to the FEC to be
                                    advertised by SR
                                    
                                    .. attribute:: fec_address
                                    
                                    	FEC that is to be advertised as part of the Prefix\-SID
                                    	**type**\: one of { str | str }
                                    
                                    

                                    """

                                    _prefix = 'mpls'
                                    _revision = '2015-11-05'

                                    def __init__(self):
                                        self.parent = None
                                        self.fec_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-mpls:config'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.fec_address is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                        return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.Config']['meta_info']


                                class PrefixSid(object):
                                    """
                                    Parameters relating to the Prefix\-SID
                                    used for the originated FEC
                                    
                                    .. attribute:: config
                                    
                                    	Configuration parameters relating to the Prefix\-SID used for the originated FEC
                                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state parameters relating to the Prefix\-SID used for the originated FEC
                                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.State>`
                                    
                                    

                                    """

                                    _prefix = 'mpls'
                                    _revision = '2015-11-05'

                                    def __init__(self):
                                        self.parent = None
                                        self.config = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.Config()
                                        self.config.parent = self
                                        self.state = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.State()
                                        self.state.parent = self


                                    class Config(object):
                                        """
                                        Configuration parameters relating to the Prefix\-SID
                                        used for the originated FEC
                                        
                                        .. attribute:: last_hop_behavior
                                        
                                        	Configuration relating to the LFIB actions for the Prefix\-SID to be used by the penultimate\-hop
                                        	**type**\: :py:class:`LastHopBehavior_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.Config.LastHopBehavior_Enum>`
                                        
                                        .. attribute:: node_flag
                                        
                                        	Specifies that the Prefix\-SID is to be treated as a Node\-SID by setting the N\-flag in the advertised Prefix\-SID TLV in the IGP
                                        	**type**\: bool
                                        
                                        .. attribute:: type
                                        
                                        	Specifies how the value of the Prefix\-SID should be interpreted \- whether as an offset to the SRGB, or as an absolute value
                                        	**type**\: :py:class:`Type_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.Config.Type_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'mpls'
                                        _revision = '2015-11-05'

                                        def __init__(self):
                                            self.parent = None
                                            self.last_hop_behavior = None
                                            self.node_flag = None
                                            self.type = None

                                        class LastHopBehavior_Enum(Enum):
                                            """
                                            LastHopBehavior_Enum

                                            Configuration relating to the LFIB actions for the
                                            Prefix\-SID to be used by the penultimate\-hop

                                            """

                                            """

                                            Specifies that the explicit null label is to be used
                                            when the penultimate hop forwards a labelled packet to
                                            this Prefix\-SID

                                            """
                                            EXPLICIT_NULL = 0

                                            """

                                            Specicies that the Prefix\-SID's label value is to be
                                            left in place when the penultimate hop forwards to this
                                            Prefix\-SID

                                            """
                                            UNCHANGED = 1

                                            """

                                            Specicies that the penultimate hop should pop the
                                            Prefix\-SID label before forwarding to the eLER

                                            """
                                            PHP = 2


                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                                return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.Config.LastHopBehavior_Enum']


                                        class Type_Enum(Enum):
                                            """
                                            Type_Enum

                                            Specifies how the value of the Prefix\-SID should be
                                            interpreted \- whether as an offset to the SRGB, or as an
                                            absolute value

                                            """

                                            """

                                            Set when the value of the prefix SID should be specified
                                            as an off\-set from the SRGB's zero\-value. When multiple
                                            SRGBs are specified, the zero\-value is the minimum
                                            of their lower bounds

                                            """
                                            INDEX = 0

                                            """

                                            Set when the value of a prefix SID is specified as the
                                            absolute value within an SRGB. It is an error to specify
                                            an absolute value outside of a specified SRGB

                                            """
                                            ABSOLUTE = 1


                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                                return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.Config.Type_Enum']


                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-mpls:config'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.last_hop_behavior is not None:
                                                return True

                                            if self.node_flag is not None:
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                            return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.Config']['meta_info']


                                    class State(object):
                                        """
                                        Operational state parameters relating to the
                                        Prefix\-SID used for the originated FEC
                                        
                                        .. attribute:: last_hop_behavior
                                        
                                        	Configuration relating to the LFIB actions for the Prefix\-SID to be used by the penultimate\-hop
                                        	**type**\: :py:class:`LastHopBehavior_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.State.LastHopBehavior_Enum>`
                                        
                                        .. attribute:: node_flag
                                        
                                        	Specifies that the Prefix\-SID is to be treated as a Node\-SID by setting the N\-flag in the advertised Prefix\-SID TLV in the IGP
                                        	**type**\: bool
                                        
                                        .. attribute:: type
                                        
                                        	Specifies how the value of the Prefix\-SID should be interpreted \- whether as an offset to the SRGB, or as an absolute value
                                        	**type**\: :py:class:`Type_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.State.Type_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'mpls'
                                        _revision = '2015-11-05'

                                        def __init__(self):
                                            self.parent = None
                                            self.last_hop_behavior = None
                                            self.node_flag = None
                                            self.type = None

                                        class LastHopBehavior_Enum(Enum):
                                            """
                                            LastHopBehavior_Enum

                                            Configuration relating to the LFIB actions for the
                                            Prefix\-SID to be used by the penultimate\-hop

                                            """

                                            """

                                            Specifies that the explicit null label is to be used
                                            when the penultimate hop forwards a labelled packet to
                                            this Prefix\-SID

                                            """
                                            EXPLICIT_NULL = 0

                                            """

                                            Specicies that the Prefix\-SID's label value is to be
                                            left in place when the penultimate hop forwards to this
                                            Prefix\-SID

                                            """
                                            UNCHANGED = 1

                                            """

                                            Specicies that the penultimate hop should pop the
                                            Prefix\-SID label before forwarding to the eLER

                                            """
                                            PHP = 2


                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                                return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.State.LastHopBehavior_Enum']


                                        class Type_Enum(Enum):
                                            """
                                            Type_Enum

                                            Specifies how the value of the Prefix\-SID should be
                                            interpreted \- whether as an offset to the SRGB, or as an
                                            absolute value

                                            """

                                            """

                                            Set when the value of the prefix SID should be specified
                                            as an off\-set from the SRGB's zero\-value. When multiple
                                            SRGBs are specified, the zero\-value is the minimum
                                            of their lower bounds

                                            """
                                            INDEX = 0

                                            """

                                            Set when the value of a prefix SID is specified as the
                                            absolute value within an SRGB. It is an error to specify
                                            an absolute value outside of a specified SRGB

                                            """
                                            ABSOLUTE = 1


                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                                return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.State.Type_Enum']


                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-mpls:state'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.last_hop_behavior is not None:
                                                return True

                                            if self.node_flag is not None:
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                            return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid.State']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-mpls:prefix-sid'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.config is not None and self.config._has_data():
                                            return True

                                        if self.config is not None and self.config.is_presence():
                                            return True

                                        if self.state is not None and self.state._has_data():
                                            return True

                                        if self.state is not None and self.state.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                        return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.PrefixSid']['meta_info']


                                class State(object):
                                    """
                                    Operational state relating to a FEC advertised by SR
                                    
                                    .. attribute:: fec_address
                                    
                                    	FEC that is to be advertised as part of the Prefix\-SID
                                    	**type**\: one of { str | str }
                                    
                                    

                                    """

                                    _prefix = 'mpls'
                                    _revision = '2015-11-05'

                                    def __init__(self):
                                        self.parent = None
                                        self.fec_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-mpls:state'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.fec_address is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                        return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec.State']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.fec_address is None:
                                        raise YPYDataValidationError('Key property fec_address is None')

                                    return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path/openconfig-mpls:path-setup-protocol/openconfig-mpls:segment-routing/openconfig-mpls:tunnel/openconfig-mpls:p2p-lsp/openconfig-mpls:fec[openconfig-mpls:fec-address = ' + str(self.fec_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.fec_address is not None:
                                        return True

                                    if self.config is not None and self.config._has_data():
                                        return True

                                    if self.config is not None and self.config.is_presence():
                                        return True

                                    if self.prefix_sid is not None and self.prefix_sid._has_data():
                                        return True

                                    if self.prefix_sid is not None and self.prefix_sid.is_presence():
                                        return True

                                    if self.state is not None and self.state._has_data():
                                        return True

                                    if self.state is not None and self.state.is_presence():
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                    return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp.Fec']['meta_info']

                            @property
                            def _common_path(self):

                                return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path/openconfig-mpls:path-setup-protocol/openconfig-mpls:segment-routing/openconfig-mpls:tunnel/openconfig-mpls:p2p-lsp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.fec is not None:
                                    for child_ref in self.fec:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2pLsp']['meta_info']

                        @property
                        def _common_path(self):

                            return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path/openconfig-mpls:path-setup-protocol/openconfig-mpls:segment-routing/openconfig-mpls:tunnel'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.p2p_lsp is not None and self.p2p_lsp._has_data():
                                return True

                            if self.p2p_lsp is not None and self.p2p_lsp.is_presence():
                                return True

                            if self.tunnel_type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel']['meta_info']

                    @property
                    def _common_path(self):

                        return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path/openconfig-mpls:path-setup-protocol/openconfig-mpls:segment-routing'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.tunnel is not None and self.tunnel._has_data():
                            return True

                        if self.tunnel is not None and self.tunnel.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return True

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting']['meta_info']

                @property
                def _common_path(self):

                    return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path/openconfig-mpls:path-setup-protocol'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ldp is not None and self.ldp._has_data():
                        return True

                    if self.ldp is not None and self.ldp.is_presence():
                        return True

                    if self.segment_routing is not None and self.segment_routing._has_data():
                        return True

                    if self.segment_routing is not None and self.segment_routing.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:lsps/openconfig-mpls:unconstrained-path'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.path_setup_protocol is not None and self.path_setup_protocol._has_data():
                    return True

                if self.path_setup_protocol is not None and self.path_setup_protocol.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.Lsps.UnconstrainedPath']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-mpls:mpls/openconfig-mpls:lsps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.constrained_path is not None and self.constrained_path._has_data():
                return True

            if self.constrained_path is not None and self.constrained_path.is_presence():
                return True

            if self.static_lsps is not None and self.static_lsps._has_data():
                return True

            if self.static_lsps is not None and self.static_lsps.is_presence():
                return True

            if self.unconstrained_path is not None and self.unconstrained_path._has_data():
                return True

            if self.unconstrained_path is not None and self.unconstrained_path.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_mpls as meta
            return meta._meta_table['Mpls.Lsps']['meta_info']


    class SignalingProtocols(object):
        """
        top\-level signaling protocol configuration
        
        .. attribute:: ldp
        
        	LDP global signaling configuration
        	**type**\: :py:class:`Ldp <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.Ldp>`
        
        .. attribute:: rsvp_te
        
        	RSVP\-TE global signaling protocol configuration
        	**type**\: :py:class:`RsvpTe <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe>`
        
        .. attribute:: segment_routing
        
        	SR global signaling config
        	**type**\: :py:class:`SegmentRouting <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting>`
        
        

        """

        _prefix = 'mpls'
        _revision = '2015-11-05'

        def __init__(self):
            self.parent = None
            self.ldp = Mpls.SignalingProtocols.Ldp()
            self.ldp.parent = self
            self.rsvp_te = Mpls.SignalingProtocols.RsvpTe()
            self.rsvp_te.parent = self
            self.segment_routing = Mpls.SignalingProtocols.SegmentRouting()
            self.segment_routing.parent = self


        class Ldp(object):
            """
            LDP global signaling configuration
            
            .. attribute:: timers
            
            	LDP timers
            	**type**\: :py:class:`Timers <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.Ldp.Timers>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.timers = Mpls.SignalingProtocols.Ldp.Timers()
                self.timers.parent = self


            class Timers(object):
                """
                LDP timers
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    pass

                @property
                def _common_path(self):

                    return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:ldp/openconfig-mpls:timers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.SignalingProtocols.Ldp.Timers']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:ldp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.timers is not None and self.timers._has_data():
                    return True

                if self.timers is not None and self.timers.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.SignalingProtocols.Ldp']['meta_info']


        class RsvpTe(object):
            """
            RSVP\-TE global signaling protocol configuration
            
            .. attribute:: global_
            
            	Platform wide RSVP configuration and state
            	**type**\: :py:class:`Global <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global>`
            
            .. attribute:: interface_attributes
            
            	Attributes relating to RSVP\-TE enabled interfaces
            	**type**\: :py:class:`InterfaceAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes>`
            
            .. attribute:: neighbors
            
            	Configuration and state for RSVP neighbors connecting to the device
            	**type**\: :py:class:`Neighbors <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors>`
            
            .. attribute:: sessions
            
            	Configuration and state of RSVP sessions
            	**type**\: :py:class:`Sessions <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.global_ = Mpls.SignalingProtocols.RsvpTe.Global()
                self.global_.parent = self
                self.interface_attributes = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes()
                self.interface_attributes.parent = self
                self.neighbors = Mpls.SignalingProtocols.RsvpTe.Neighbors()
                self.neighbors.parent = self
                self.sessions = Mpls.SignalingProtocols.RsvpTe.Sessions()
                self.sessions.parent = self


            class Global(object):
                """
                Platform wide RSVP configuration and state
                
                .. attribute:: graceful_restart
                
                	Operational state and configuration parameters relating to graceful\-restart for RSVP
                	**type**\: :py:class:`GracefulRestart <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart>`
                
                .. attribute:: hellos
                
                	Top level container for RSVP hello parameters
                	**type**\: :py:class:`Hellos <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.Hellos>`
                
                .. attribute:: soft_preemption
                
                	Protocol options relating to RSVP soft preemption
                	**type**\: :py:class:`SoftPreemption <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption>`
                
                .. attribute:: state
                
                	Platform wide RSVP state, including counters
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.graceful_restart = Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart()
                    self.graceful_restart.parent = self
                    self.hellos = Mpls.SignalingProtocols.RsvpTe.Global.Hellos()
                    self.hellos.parent = self
                    self.soft_preemption = Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption()
                    self.soft_preemption.parent = self
                    self.state = Mpls.SignalingProtocols.RsvpTe.Global.State()
                    self.state.parent = self


                class GracefulRestart(object):
                    """
                    Operational state and configuration parameters relating to
                    graceful\-restart for RSVP
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to graceful\-restart
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.Config>`
                    
                    .. attribute:: state
                    
                    	State information associated with RSVP graceful\-restart
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.config = Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.Config()
                        self.config.parent = self
                        self.state = Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to
                        graceful\-restart
                        
                        .. attribute:: enable
                        
                        	Enables graceful restart on the node
                        	**type**\: bool
                        
                        .. attribute:: recovery_time
                        
                        	RSVP state recovery time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: restart_time
                        
                        	Graceful restart time (seconds)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.enable = None
                            self.recovery_time = None
                            self.restart_time = None

                        @property
                        def _common_path(self):

                            return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:graceful-restart/openconfig-mpls:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.enable is not None:
                                return True

                            if self.recovery_time is not None:
                                return True

                            if self.restart_time is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.Config']['meta_info']


                    class State(object):
                        """
                        State information associated with
                        RSVP graceful\-restart
                        
                        .. attribute:: enable
                        
                        	Enables graceful restart on the node
                        	**type**\: bool
                        
                        .. attribute:: recovery_time
                        
                        	RSVP state recovery time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: restart_time
                        
                        	Graceful restart time (seconds)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.enable = None
                            self.recovery_time = None
                            self.restart_time = None

                        @property
                        def _common_path(self):

                            return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:graceful-restart/openconfig-mpls:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.enable is not None:
                                return True

                            if self.recovery_time is not None:
                                return True

                            if self.restart_time is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.State']['meta_info']

                    @property
                    def _common_path(self):

                        return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:graceful-restart'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.config is not None and self.config.is_presence():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.state is not None and self.state.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart']['meta_info']


                class Hellos(object):
                    """
                    Top level container for RSVP hello parameters
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to RSVP hellos
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.Hellos.Config>`
                    
                    .. attribute:: state
                    
                    	State information associated with RSVP hellos
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.Hellos.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.config = Mpls.SignalingProtocols.RsvpTe.Global.Hellos.Config()
                        self.config.parent = self
                        self.state = Mpls.SignalingProtocols.RsvpTe.Global.Hellos.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to RSVP
                        hellos
                        
                        .. attribute:: hello_interval
                        
                        	set the interval in ms between RSVP hello messages
                        	**type**\: int
                        
                        	**range:** 1000..60000
                        
                        .. attribute:: refresh_reduction
                        
                        	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.hello_interval = None
                            self.refresh_reduction = None

                        @property
                        def _common_path(self):

                            return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:hellos/openconfig-mpls:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.hello_interval is not None:
                                return True

                            if self.refresh_reduction is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.Hellos.Config']['meta_info']


                    class State(object):
                        """
                        State information associated with RSVP hellos
                        
                        .. attribute:: hello_interval
                        
                        	set the interval in ms between RSVP hello messages
                        	**type**\: int
                        
                        	**range:** 1000..60000
                        
                        .. attribute:: refresh_reduction
                        
                        	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.hello_interval = None
                            self.refresh_reduction = None

                        @property
                        def _common_path(self):

                            return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:hellos/openconfig-mpls:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.hello_interval is not None:
                                return True

                            if self.refresh_reduction is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.Hellos.State']['meta_info']

                    @property
                    def _common_path(self):

                        return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:hellos'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.config is not None and self.config.is_presence():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.state is not None and self.state.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.Hellos']['meta_info']


                class SoftPreemption(object):
                    """
                    Protocol options relating to RSVP
                    soft preemption
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to RSVP soft preemption support
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters relating to RSVP soft preemption support
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.config = Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.Config()
                        self.config.parent = self
                        self.state = Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to RSVP
                        soft preemption support
                        
                        .. attribute:: enable
                        
                        	Enables soft preemption on a node
                        	**type**\: bool
                        
                        .. attribute:: soft_preemption_timeout
                        
                        	Timeout value for soft preemption to revert to hard preemption
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.enable = None
                            self.soft_preemption_timeout = None

                        @property
                        def _common_path(self):

                            return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:soft-preemption/openconfig-mpls:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.enable is not None:
                                return True

                            if self.soft_preemption_timeout is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.Config']['meta_info']


                    class State(object):
                        """
                        State parameters relating to RSVP
                        soft preemption support
                        
                        .. attribute:: enable
                        
                        	Enables soft preemption on a node
                        	**type**\: bool
                        
                        .. attribute:: soft_preemption_timeout
                        
                        	Timeout value for soft preemption to revert to hard preemption
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.enable = None
                            self.soft_preemption_timeout = None

                        @property
                        def _common_path(self):

                            return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:soft-preemption/openconfig-mpls:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.enable is not None:
                                return True

                            if self.soft_preemption_timeout is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.State']['meta_info']

                    @property
                    def _common_path(self):

                        return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:soft-preemption'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.config is not None and self.config.is_presence():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.state is not None and self.state.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption']['meta_info']


                class State(object):
                    """
                    Platform wide RSVP state, including counters
                    
                    .. attribute:: counters
                    
                    	Platform wide RSVP statistics and counters
                    	**type**\: :py:class:`Counters <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.State.Counters>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.counters = Mpls.SignalingProtocols.RsvpTe.Global.State.Counters()
                        self.counters.parent = self


                    class Counters(object):
                        """
                        Platform wide RSVP statistics and counters
                        
                        .. attribute:: in_ack_messages
                        
                        	Number of received RSVP refresh reduction ack messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_hello_messages
                        
                        	Number of received RSVP hello messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_path_error_messages
                        
                        	Number of received RSVP Path Error messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_path_messages
                        
                        	Number of received RSVP Path messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_path_tear_messages
                        
                        	Number of received RSVP Path Tear messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_reservation_error_messages
                        
                        	Number of received RSVP Resv Error messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_reservation_messages
                        
                        	Number of received RSVP Resv messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_reservation_tear_messages
                        
                        	Number of received RSVP Resv Tear messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_srefresh_messages
                        
                        	Number of received RSVP summary refresh messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_ack_messages
                        
                        	Number of sent RSVP refresh reduction ack messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_hello_messages
                        
                        	Number of sent RSVP hello messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_path_error_messages
                        
                        	Number of sent RSVP Path Error messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_path_messages
                        
                        	Number of sent RSVP PATH messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_path_tear_messages
                        
                        	Number of sent RSVP Path Tear messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_reservation_error_messages
                        
                        	Number of sent RSVP Resv Error messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_reservation_messages
                        
                        	Number of sent RSVP Resv messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_reservation_tear_messages
                        
                        	Number of sent RSVP Resv Tear messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_srefresh_messages
                        
                        	Number of sent RSVP summary refresh messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: path_timeouts
                        
                        	TODO
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: rate_limited_messages
                        
                        	RSVP messages dropped due to rate limiting
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: reservation_timeouts
                        
                        	TODO
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.in_ack_messages = None
                            self.in_hello_messages = None
                            self.in_path_error_messages = None
                            self.in_path_messages = None
                            self.in_path_tear_messages = None
                            self.in_reservation_error_messages = None
                            self.in_reservation_messages = None
                            self.in_reservation_tear_messages = None
                            self.in_srefresh_messages = None
                            self.out_ack_messages = None
                            self.out_hello_messages = None
                            self.out_path_error_messages = None
                            self.out_path_messages = None
                            self.out_path_tear_messages = None
                            self.out_reservation_error_messages = None
                            self.out_reservation_messages = None
                            self.out_reservation_tear_messages = None
                            self.out_srefresh_messages = None
                            self.path_timeouts = None
                            self.rate_limited_messages = None
                            self.reservation_timeouts = None

                        @property
                        def _common_path(self):

                            return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:state/openconfig-mpls:counters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.in_ack_messages is not None:
                                return True

                            if self.in_hello_messages is not None:
                                return True

                            if self.in_path_error_messages is not None:
                                return True

                            if self.in_path_messages is not None:
                                return True

                            if self.in_path_tear_messages is not None:
                                return True

                            if self.in_reservation_error_messages is not None:
                                return True

                            if self.in_reservation_messages is not None:
                                return True

                            if self.in_reservation_tear_messages is not None:
                                return True

                            if self.in_srefresh_messages is not None:
                                return True

                            if self.out_ack_messages is not None:
                                return True

                            if self.out_hello_messages is not None:
                                return True

                            if self.out_path_error_messages is not None:
                                return True

                            if self.out_path_messages is not None:
                                return True

                            if self.out_path_tear_messages is not None:
                                return True

                            if self.out_reservation_error_messages is not None:
                                return True

                            if self.out_reservation_messages is not None:
                                return True

                            if self.out_reservation_tear_messages is not None:
                                return True

                            if self.out_srefresh_messages is not None:
                                return True

                            if self.path_timeouts is not None:
                                return True

                            if self.rate_limited_messages is not None:
                                return True

                            if self.reservation_timeouts is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.State.Counters']['meta_info']

                    @property
                    def _common_path(self):

                        return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.counters is not None and self.counters._has_data():
                            return True

                        if self.counters is not None and self.counters.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global.State']['meta_info']

                @property
                def _common_path(self):

                    return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:global'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.graceful_restart is not None and self.graceful_restart._has_data():
                        return True

                    if self.graceful_restart is not None and self.graceful_restart.is_presence():
                        return True

                    if self.hellos is not None and self.hellos._has_data():
                        return True

                    if self.hellos is not None and self.hellos.is_presence():
                        return True

                    if self.soft_preemption is not None and self.soft_preemption._has_data():
                        return True

                    if self.soft_preemption is not None and self.soft_preemption.is_presence():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Global']['meta_info']


            class InterfaceAttributes(object):
                """
                Attributes relating to RSVP\-TE enabled interfaces
                
                .. attribute:: interface
                
                	list of per\-interface RSVP configurations
                	**type**\: list of :py:class:`Interface <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    list of per\-interface RSVP configurations
                    
                    .. attribute:: interface_name
                    
                    	references a configured IP interface
                    	**type**\: str
                    
                    .. attribute:: authentication
                    
                    	Configuration and state parameters relating to RSVP authentication as per RFC2747
                    	**type**\: :py:class:`Authentication <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication>`
                    
                    .. attribute:: config
                    
                    	Configuration of per\-interface RSVP parameters
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config>`
                    
                    .. attribute:: hellos
                    
                    	Top level container for RSVP hello parameters
                    	**type**\: :py:class:`Hellos <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos>`
                    
                    .. attribute:: protection
                    
                    	link\-protection (NHOP) related configuration
                    	**type**\: :py:class:`Protection <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection>`
                    
                    .. attribute:: state
                    
                    	Per\-interface RSVP protocol and state information
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State>`
                    
                    .. attribute:: subscription
                    
                    	Bandwidth percentage reservable by RSVP on an interface
                    	**type**\: :py:class:`Subscription <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.authentication = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication()
                        self.authentication.parent = self
                        self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config()
                        self.config.parent = self
                        self.hellos = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos()
                        self.hellos.parent = self
                        self.protection = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection()
                        self.protection.parent = self
                        self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State()
                        self.state.parent = self
                        self.subscription = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription()
                        self.subscription.parent = self


                    class Authentication(object):
                        """
                        Configuration and state parameters relating to RSVP
                        authentication as per RFC2747
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to authentication
                        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config>`
                        
                        .. attribute:: state
                        
                        	State information associated with authentication
                        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config()
                            self.config.parent = self
                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration parameters relating
                            to authentication
                            
                            .. attribute:: authentication_key
                            
                            	authenticate RSVP signaling messages
                            	**type**\: str
                            
                            	**range:** 1..32
                            
                            .. attribute:: enable
                            
                            	Enables RSVP authentication on the node
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.authentication_key = None
                                self.enable = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.authentication_key is not None:
                                    return True

                                if self.enable is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config']['meta_info']


                        class State(object):
                            """
                            State information associated
                            with authentication
                            
                            .. attribute:: authentication_key
                            
                            	authenticate RSVP signaling messages
                            	**type**\: str
                            
                            	**range:** 1..32
                            
                            .. attribute:: enable
                            
                            	Enables RSVP authentication on the node
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.authentication_key = None
                                self.enable = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.authentication_key is not None:
                                    return True

                                if self.enable is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:authentication'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.config is not None and self.config.is_presence():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.state is not None and self.state.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication']['meta_info']


                    class Config(object):
                        """
                        Configuration of per\-interface RSVP parameters
                        
                        .. attribute:: interface_name
                        
                        	Name of configured IP interface
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.interface_name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config']['meta_info']


                    class Hellos(object):
                        """
                        Top level container for RSVP hello parameters
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to RSVP hellos
                        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config>`
                        
                        .. attribute:: state
                        
                        	State information associated with RSVP hellos
                        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config()
                            self.config.parent = self
                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration parameters relating to RSVP
                            hellos
                            
                            .. attribute:: hello_interval
                            
                            	set the interval in ms between RSVP hello messages
                            	**type**\: int
                            
                            	**range:** 1000..60000
                            
                            .. attribute:: refresh_reduction
                            
                            	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.hello_interval = None
                                self.refresh_reduction = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.hello_interval is not None:
                                    return True

                                if self.refresh_reduction is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config']['meta_info']


                        class State(object):
                            """
                            State information associated with RSVP hellos
                            
                            .. attribute:: hello_interval
                            
                            	set the interval in ms between RSVP hello messages
                            	**type**\: int
                            
                            	**range:** 1000..60000
                            
                            .. attribute:: refresh_reduction
                            
                            	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.hello_interval = None
                                self.refresh_reduction = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.hello_interval is not None:
                                    return True

                                if self.refresh_reduction is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:hellos'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.config is not None and self.config.is_presence():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.state is not None and self.state.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos']['meta_info']


                    class Protection(object):
                        """
                        link\-protection (NHOP) related configuration
                        
                        .. attribute:: config
                        
                        	Configuration for link\-protection
                        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config>`
                        
                        .. attribute:: state
                        
                        	State for link\-protection
                        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config()
                            self.config.parent = self
                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration for link\-protection
                            
                            .. attribute:: bypass_optimize_interval
                            
                            	interval between periodic optimization of the bypass LSPs
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: link_protection_style_requested
                            
                            	Style of mpls frr protection desired\: link, link\-node, or unprotected
                            	**type**\: :py:class:`ProtectionType_Identity <ydk.models.openconfig.openconfig_mpls_types.ProtectionType_Identity>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.bypass_optimize_interval = None
                                self.link_protection_style_requested = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.bypass_optimize_interval is not None:
                                    return True

                                if self.link_protection_style_requested is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config']['meta_info']


                        class State(object):
                            """
                            State for link\-protection
                            
                            .. attribute:: bypass_optimize_interval
                            
                            	interval between periodic optimization of the bypass LSPs
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: link_protection_style_requested
                            
                            	Style of mpls frr protection desired\: link, link\-node, or unprotected
                            	**type**\: :py:class:`ProtectionType_Identity <ydk.models.openconfig.openconfig_mpls_types.ProtectionType_Identity>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.bypass_optimize_interval = None
                                self.link_protection_style_requested = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.bypass_optimize_interval is not None:
                                    return True

                                if self.link_protection_style_requested is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:protection'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.config is not None and self.config.is_presence():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.state is not None and self.state.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection']['meta_info']


                    class State(object):
                        """
                        Per\-interface RSVP protocol and state information
                        
                        .. attribute:: active_reservation_count
                        
                        	Number of active RSVP reservations
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: bandwidth
                        
                        	Available and reserved bandwidth by priority on the interface
                        	**type**\: list of :py:class:`Bandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth>`
                        
                        .. attribute:: counters
                        
                        	Interface specific RSVP statistics and counters
                        	**type**\: :py:class:`Counters <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters>`
                        
                        .. attribute:: highwater_mark
                        
                        	Maximum bandwidth ever reserved
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.active_reservation_count = None
                            self.bandwidth = YList()
                            self.bandwidth.parent = self
                            self.bandwidth.name = 'bandwidth'
                            self.counters = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters()
                            self.counters.parent = self
                            self.highwater_mark = None


                        class Bandwidth(object):
                            """
                            Available and reserved bandwidth by priority on
                            the interface.
                            
                            .. attribute:: priority
                            
                            	RSVP priority level for LSPs traversing the interface
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: available_bandwidth
                            
                            	Bandwidth currently available
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: reserved_bandwidth
                            
                            	Bandwidth currently reserved
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.priority = None
                                self.available_bandwidth = None
                                self.reserved_bandwidth = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.priority is None:
                                    raise YPYDataValidationError('Key property priority is None')

                                return self.parent._common_path +'/openconfig-mpls:bandwidth[openconfig-mpls:priority = ' + str(self.priority) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.priority is not None:
                                    return True

                                if self.available_bandwidth is not None:
                                    return True

                                if self.reserved_bandwidth is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth']['meta_info']


                        class Counters(object):
                            """
                            Interface specific RSVP statistics and counters
                            
                            .. attribute:: in_ack_messages
                            
                            	Number of received RSVP refresh reduction ack messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_hello_messages
                            
                            	Number of received RSVP hello messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_path_error_messages
                            
                            	Number of received RSVP Path Error messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_path_messages
                            
                            	Number of received RSVP Path messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_path_tear_messages
                            
                            	Number of received RSVP Path Tear messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_reservation_error_messages
                            
                            	Number of received RSVP Resv Error messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_reservation_messages
                            
                            	Number of received RSVP Resv messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_reservation_tear_messages
                            
                            	Number of received RSVP Resv Tear messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_srefresh_messages
                            
                            	Number of received RSVP summary refresh messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_ack_messages
                            
                            	Number of sent RSVP refresh reduction ack messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_hello_messages
                            
                            	Number of sent RSVP hello messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_path_error_messages
                            
                            	Number of sent RSVP Path Error messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_path_messages
                            
                            	Number of sent RSVP PATH messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_path_tear_messages
                            
                            	Number of sent RSVP Path Tear messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_reservation_error_messages
                            
                            	Number of sent RSVP Resv Error messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_reservation_messages
                            
                            	Number of sent RSVP Resv messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_reservation_tear_messages
                            
                            	Number of sent RSVP Resv Tear messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_srefresh_messages
                            
                            	Number of sent RSVP summary refresh messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.in_ack_messages = None
                                self.in_hello_messages = None
                                self.in_path_error_messages = None
                                self.in_path_messages = None
                                self.in_path_tear_messages = None
                                self.in_reservation_error_messages = None
                                self.in_reservation_messages = None
                                self.in_reservation_tear_messages = None
                                self.in_srefresh_messages = None
                                self.out_ack_messages = None
                                self.out_hello_messages = None
                                self.out_path_error_messages = None
                                self.out_path_messages = None
                                self.out_path_tear_messages = None
                                self.out_reservation_error_messages = None
                                self.out_reservation_messages = None
                                self.out_reservation_tear_messages = None
                                self.out_srefresh_messages = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:counters'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.in_ack_messages is not None:
                                    return True

                                if self.in_hello_messages is not None:
                                    return True

                                if self.in_path_error_messages is not None:
                                    return True

                                if self.in_path_messages is not None:
                                    return True

                                if self.in_path_tear_messages is not None:
                                    return True

                                if self.in_reservation_error_messages is not None:
                                    return True

                                if self.in_reservation_messages is not None:
                                    return True

                                if self.in_reservation_tear_messages is not None:
                                    return True

                                if self.in_srefresh_messages is not None:
                                    return True

                                if self.out_ack_messages is not None:
                                    return True

                                if self.out_hello_messages is not None:
                                    return True

                                if self.out_path_error_messages is not None:
                                    return True

                                if self.out_path_messages is not None:
                                    return True

                                if self.out_path_tear_messages is not None:
                                    return True

                                if self.out_reservation_error_messages is not None:
                                    return True

                                if self.out_reservation_messages is not None:
                                    return True

                                if self.out_reservation_tear_messages is not None:
                                    return True

                                if self.out_srefresh_messages is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.active_reservation_count is not None:
                                return True

                            if self.bandwidth is not None:
                                for child_ref in self.bandwidth:
                                    if child_ref._has_data():
                                        return True

                            if self.counters is not None and self.counters._has_data():
                                return True

                            if self.counters is not None and self.counters.is_presence():
                                return True

                            if self.highwater_mark is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State']['meta_info']


                    class Subscription(object):
                        """
                        Bandwidth percentage reservable by RSVP
                        on an interface
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to RSVP subscription options
                        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to RSVP subscription options
                        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config()
                            self.config.parent = self
                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration parameters relating to RSVP
                            subscription options
                            
                            .. attribute:: subscription
                            
                            	percentage of the interface bandwidth that RSVP can reserve
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.subscription = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.subscription is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config']['meta_info']


                        class State(object):
                            """
                            State parameters relating to RSVP
                            subscription options
                            
                            .. attribute:: subscription
                            
                            	percentage of the interface bandwidth that RSVP can reserve
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.subscription = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.subscription is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:subscription'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.config is not None and self.config.is_presence():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.state is not None and self.state.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription']['meta_info']

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYDataValidationError('Key property interface_name is None')

                        return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:interface-attributes/openconfig-mpls:interface[openconfig-mpls:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.interface_name is not None:
                            return True

                        if self.authentication is not None and self.authentication._has_data():
                            return True

                        if self.authentication is not None and self.authentication.is_presence():
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.config is not None and self.config.is_presence():
                            return True

                        if self.hellos is not None and self.hellos._has_data():
                            return True

                        if self.hellos is not None and self.hellos.is_presence():
                            return True

                        if self.protection is not None and self.protection._has_data():
                            return True

                        if self.protection is not None and self.protection.is_presence():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.state is not None and self.state.is_presence():
                            return True

                        if self.subscription is not None and self.subscription._has_data():
                            return True

                        if self.subscription is not None and self.subscription.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface']['meta_info']

                @property
                def _common_path(self):

                    return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:interface-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes']['meta_info']


            class Neighbors(object):
                """
                Configuration and state for RSVP neighbors connecting
                to the device
                
                .. attribute:: config
                
                	Configuration of RSVP neighbor information
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.Config>`
                
                .. attribute:: state
                
                	State information relating to RSVP neighbors
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.config = Mpls.SignalingProtocols.RsvpTe.Neighbors.Config()
                    self.config.parent = self
                    self.state = Mpls.SignalingProtocols.RsvpTe.Neighbors.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration of RSVP neighbor information
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        pass

                    @property
                    def _common_path(self):

                        return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:neighbors/openconfig-mpls:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors.Config']['meta_info']


                class State(object):
                    """
                    State information relating to RSVP neighbors
                    
                    .. attribute:: neighbor
                    
                    	List of RSVP neighbors connecting to the device, keyed by neighbor address
                    	**type**\: list of :py:class:`Neighbor <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.neighbor = YList()
                        self.neighbor.parent = self
                        self.neighbor.name = 'neighbor'


                    class Neighbor(object):
                        """
                        List of RSVP neighbors connecting to the device,
                        keyed by neighbor address
                        
                        .. attribute:: address
                        
                        	Address of RSVP neighbor
                        	**type**\: one of { str | str }
                        
                        .. attribute:: detected_interface
                        
                        	Interface where RSVP neighbor was detected
                        	**type**\: str
                        
                        .. attribute:: neighbor_status
                        
                        	Enumuration of possible RSVP neighbor states
                        	**type**\: :py:class:`NeighborStatus_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor.NeighborStatus_Enum>`
                        
                        .. attribute:: refresh_reduction
                        
                        	Suppport of neighbor for RSVP refresh reduction
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.detected_interface = None
                            self.neighbor_status = None
                            self.refresh_reduction = None

                        class NeighborStatus_Enum(Enum):
                            """
                            NeighborStatus_Enum

                            Enumuration of possible RSVP neighbor states

                            """

                            """

                            RSVP hello messages are detected from the neighbor

                            """
                            UP = 0

                            """

                            RSVP neighbor not detected as up, due to a
                            communication failure or IGP notification
                            the neighbor is unavailable

                            """
                            DOWN = 1


                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor.NeighborStatus_Enum']


                        @property
                        def _common_path(self):
                            if self.address is None:
                                raise YPYDataValidationError('Key property address is None')

                            return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:neighbors/openconfig-mpls:state/openconfig-mpls:neighbor[openconfig-mpls:address = ' + str(self.address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.address is not None:
                                return True

                            if self.detected_interface is not None:
                                return True

                            if self.neighbor_status is not None:
                                return True

                            if self.refresh_reduction is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:neighbors/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.neighbor is not None:
                            for child_ref in self.neighbor:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors.State']['meta_info']

                @property
                def _common_path(self):

                    return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:neighbors'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.config is not None and self.config.is_presence():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors']['meta_info']


            class Sessions(object):
                """
                Configuration and state of RSVP sessions
                
                .. attribute:: config
                
                	Configuration of RSVP sessions on the device
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Config>`
                
                .. attribute:: state
                
                	State information relating to RSVP sessions on the device
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.config = Mpls.SignalingProtocols.RsvpTe.Sessions.Config()
                    self.config.parent = self
                    self.state = Mpls.SignalingProtocols.RsvpTe.Sessions.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration of RSVP sessions on the device
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        pass

                    @property
                    def _common_path(self):

                        return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:sessions/openconfig-mpls:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions.Config']['meta_info']


                class State(object):
                    """
                    State information relating to RSVP sessions
                    on the device
                    
                    .. attribute:: session
                    
                    	List of RSVP sessions
                    	**type**\: list of :py:class:`Session <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.session = YList()
                        self.session.parent = self
                        self.session.name = 'session'


                    class Session(object):
                        """
                        List of RSVP sessions
                        
                        .. attribute:: destination_address
                        
                        	Destination address of RSVP session
                        	**type**\: one of { str | str }
                        
                        .. attribute:: destination_port
                        
                        	RSVP source port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: source_address
                        
                        	Origin address of RSVP session
                        	**type**\: one of { str | str }
                        
                        .. attribute:: source_port
                        
                        	RSVP source port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: associated_lsps
                        
                        	List of label switched paths associated with this RSVP session
                        	**type**\: list of str
                        
                        .. attribute:: label_in
                        
                        	Incoming MPLS label associated with this RSVP session
                        	**type**\: one of { int | :py:class:`MplsLabel_Enum <ydk.models.openconfig.openconfig_mpls_types.MplsLabel_Enum>` }
                        
                        .. attribute:: label_out
                        
                        	Outgoing MPLS label associated with this RSVP session
                        	**type**\: one of { int | :py:class:`MplsLabel_Enum <ydk.models.openconfig.openconfig_mpls_types.MplsLabel_Enum>` }
                        
                        .. attribute:: status
                        
                        	Enumeration of RSVP session states
                        	**type**\: :py:class:`Status_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session.Status_Enum>`
                        
                        .. attribute:: tunnel_id
                        
                        	Unique identifier of RSVP session
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: type
                        
                        	Enumeration of possible RSVP session types
                        	**type**\: :py:class:`Type_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session.Type_Enum>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.destination_address = None
                            self.destination_port = None
                            self.source_address = None
                            self.source_port = None
                            self.associated_lsps = []
                            self.label_in = None
                            self.label_out = None
                            self.status = None
                            self.tunnel_id = None
                            self.type = None

                        class Status_Enum(Enum):
                            """
                            Status_Enum

                            Enumeration of RSVP session states

                            """

                            """

                            RSVP session is up

                            """
                            UP = 0

                            """

                            RSVP session is down

                            """
                            DOWN = 1


                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session.Status_Enum']


                        class Type_Enum(Enum):
                            """
                            Type_Enum

                            Enumeration of possible RSVP session types

                            """

                            """

                            RSVP session originates on this device

                            """
                            SOURCE = 0

                            """

                            RSVP session transits this device only

                            """
                            TRANSIT = 1

                            """

                            RSVP session terminates on this device

                            """
                            DESTINATION = 2


                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session.Type_Enum']


                        @property
                        def _common_path(self):
                            if self.destination_address is None:
                                raise YPYDataValidationError('Key property destination_address is None')
                            if self.destination_port is None:
                                raise YPYDataValidationError('Key property destination_port is None')
                            if self.source_address is None:
                                raise YPYDataValidationError('Key property source_address is None')
                            if self.source_port is None:
                                raise YPYDataValidationError('Key property source_port is None')

                            return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:sessions/openconfig-mpls:state/openconfig-mpls:session[openconfig-mpls:destination-address = ' + str(self.destination_address) + '][openconfig-mpls:destination-port = ' + str(self.destination_port) + '][openconfig-mpls:source-address = ' + str(self.source_address) + '][openconfig-mpls:source-port = ' + str(self.source_port) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.destination_address is not None:
                                return True

                            if self.destination_port is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.source_port is not None:
                                return True

                            if self.associated_lsps is not None:
                                for child in self.associated_lsps:
                                    if child is not None:
                                        return True

                            if self.label_in is not None:
                                return True

                            if self.label_out is not None:
                                return True

                            if self.status is not None:
                                return True

                            if self.tunnel_id is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session']['meta_info']

                    @property
                    def _common_path(self):

                        return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:sessions/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.session is not None:
                            for child_ref in self.session:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions.State']['meta_info']

                @property
                def _common_path(self):

                    return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te/openconfig-mpls:sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.config is not None and self.config.is_presence():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:rsvp-te'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.global_ is not None and self.global_._has_data():
                    return True

                if self.global_ is not None and self.global_.is_presence():
                    return True

                if self.interface_attributes is not None and self.interface_attributes._has_data():
                    return True

                if self.interface_attributes is not None and self.interface_attributes.is_presence():
                    return True

                if self.neighbors is not None and self.neighbors._has_data():
                    return True

                if self.neighbors is not None and self.neighbors.is_presence():
                    return True

                if self.sessions is not None and self.sessions._has_data():
                    return True

                if self.sessions is not None and self.sessions.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.SignalingProtocols.RsvpTe']['meta_info']


        class SegmentRouting(object):
            """
            SR global signaling config
            
            .. attribute:: interfaces
            
            	List of interfaces with associated segment routing configuration
            	**type**\: list of :py:class:`Interfaces <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces>`
            
            .. attribute:: srgb
            
            	List of Segment Routing Global Block (SRGB) entries. These label blocks are reserved to be allocated as domain\-wide entries
            	**type**\: list of :py:class:`Srgb <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Srgb>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.interfaces = YList()
                self.interfaces.parent = self
                self.interfaces.name = 'interfaces'
                self.srgb = YList()
                self.srgb.parent = self
                self.srgb.name = 'srgb'


            class Interfaces(object):
                """
                List of interfaces with associated segment routing
                configuration
                
                .. attribute:: interface
                
                	Reference to the interface for which segment routing configuration is to be applied
                	**type**\: str
                
                .. attribute:: adjacency_sid
                
                	Configuration for Adjacency SIDs that are related to the specified interface
                	**type**\: :py:class:`AdjacencySid <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid>`
                
                .. attribute:: config
                
                	Interface configuration parameters for Segment Routing relating to the specified interface
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config>`
                
                .. attribute:: state
                
                	State parameters for Segment Routing features relating to the specified interface
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.interface = None
                    self.adjacency_sid = Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid()
                    self.adjacency_sid.parent = self
                    self.config = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config()
                    self.config.parent = self
                    self.state = Mpls.SignalingProtocols.SegmentRouting.Interfaces.State()
                    self.state.parent = self


                class AdjacencySid(object):
                    """
                    Configuration for Adjacency SIDs that are related to
                    the specified interface
                    
                    .. attribute:: config
                    
                    	Configuration parameters for the Adjacency\-SIDs that are related to this interface
                    	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters for the Adjacency\-SIDs that are related to this interface
                    	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.config = Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config()
                        self.config.parent = self
                        self.state = Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters for the Adjacency\-SIDs
                        that are related to this interface
                        
                        .. attribute:: advertise
                        
                        	Specifies the type of adjacency SID which should be advertised for the specified entity
                        	**type**\: list of :py:class:`Advertise_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config.Advertise_Enum>`
                        
                        .. attribute:: groups
                        
                        	Specifies the groups to which this interface belongs. Setting a value in this list results in an additional AdjSID being advertised, with the S\-bit set to 1. The AdjSID is assumed to be protected
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.advertise = []
                            self.groups = []

                        class Advertise_Enum(Enum):
                            """
                            Advertise_Enum

                            Specifies the type of adjacency SID which should be
                            advertised for the specified entity.

                            """

                            """

                            Advertise an Adjacency\-SID for this interface, which is
                            eligible to be protected using a local protection
                            mechanism on the local LSR. The local protection
                            mechanism selected is dependent upon the configuration
                            of RSVP\-TE FRR or LFA elsewhere on the system

                            """
                            PROTECTED = 0

                            """

                            Advertise an Adajcency\-SID for this interface, which is
                            explicitly excluded from being protected by any local
                            protection mechanism

                            """
                            UNPROTECTED = 1


                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config.Advertise_Enum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.advertise is not None:
                                for child in self.advertise:
                                    if child is not None:
                                        return True

                            if self.groups is not None:
                                for child in self.groups:
                                    if child is not None:
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config']['meta_info']


                    class State(object):
                        """
                        State parameters for the Adjacency\-SIDs that are
                        related to this interface
                        
                        .. attribute:: advertise
                        
                        	Specifies the type of adjacency SID which should be advertised for the specified entity
                        	**type**\: list of :py:class:`Advertise_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State.Advertise_Enum>`
                        
                        .. attribute:: groups
                        
                        	Specifies the groups to which this interface belongs. Setting a value in this list results in an additional AdjSID being advertised, with the S\-bit set to 1. The AdjSID is assumed to be protected
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.advertise = []
                            self.groups = []

                        class Advertise_Enum(Enum):
                            """
                            Advertise_Enum

                            Specifies the type of adjacency SID which should be
                            advertised for the specified entity.

                            """

                            """

                            Advertise an Adjacency\-SID for this interface, which is
                            eligible to be protected using a local protection
                            mechanism on the local LSR. The local protection
                            mechanism selected is dependent upon the configuration
                            of RSVP\-TE FRR or LFA elsewhere on the system

                            """
                            PROTECTED = 0

                            """

                            Advertise an Adajcency\-SID for this interface, which is
                            explicitly excluded from being protected by any local
                            protection mechanism

                            """
                            UNPROTECTED = 1


                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State.Advertise_Enum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-mpls:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.advertise is not None:
                                for child in self.advertise:
                                    if child is not None:
                                        return True

                            if self.groups is not None:
                                for child in self.groups:
                                    if child is not None:
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:adjacency-sid'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.config is not None and self.config.is_presence():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.state is not None and self.state.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid']['meta_info']


                class Config(object):
                    """
                    Interface configuration parameters for Segment Routing
                    relating to the specified interface
                    
                    .. attribute:: interface
                    
                    	Reference to the interface for which segment routing configuration is to be applied
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.interface = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.interface is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config']['meta_info']


                class State(object):
                    """
                    State parameters for Segment Routing features relating
                    to the specified interface
                    
                    .. attribute:: interface
                    
                    	Reference to the interface for which segment routing configuration is to be applied
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.interface = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.interface is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.State']['meta_info']

                @property
                def _common_path(self):
                    if self.interface is None:
                        raise YPYDataValidationError('Key property interface is None')

                    return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:segment-routing/openconfig-mpls:interfaces[openconfig-mpls:interface = ' + str(self.interface) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.interface is not None:
                        return True

                    if self.adjacency_sid is not None and self.adjacency_sid._has_data():
                        return True

                    if self.adjacency_sid is not None and self.adjacency_sid.is_presence():
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.config is not None and self.config.is_presence():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces']['meta_info']


            class Srgb(object):
                """
                List of Segment Routing Global Block (SRGB) entries. These
                label blocks are reserved to be allocated as domain\-wide
                entries.
                
                .. attribute:: lower_bound
                
                	Lower value in the block
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: upper_bound
                
                	Upper value in the block
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: config
                
                	Configuration parameters relating to the Segment Routing Global Block (SRGB)
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Srgb.Config>`
                
                .. attribute:: state
                
                	State parameters relating to the Segment Routing Global Block (SRGB)
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Srgb.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.lower_bound = None
                    self.upper_bound = None
                    self.config = Mpls.SignalingProtocols.SegmentRouting.Srgb.Config()
                    self.config.parent = self
                    self.state = Mpls.SignalingProtocols.SegmentRouting.Srgb.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to the Segment Routing
                    Global Block (SRGB)
                    
                    .. attribute:: lower_bound
                    
                    	Lower value in the block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: upper_bound
                    
                    	Upper value in the block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.lower_bound = None
                        self.upper_bound = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.lower_bound is not None:
                            return True

                        if self.upper_bound is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Srgb.Config']['meta_info']


                class State(object):
                    """
                    State parameters relating to the Segment Routing Global
                    Block (SRGB)
                    
                    .. attribute:: free
                    
                    	Number of SRGB indexes that have not yet been allocated
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lower_bound
                    
                    	Lower value in the block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: size
                    
                    	Number of indexes in the SRGB block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: upper_bound
                    
                    	Upper value in the block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: used
                    
                    	Number of SRGB indexes that are currently allocated
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.free = None
                        self.lower_bound = None
                        self.size = None
                        self.upper_bound = None
                        self.used = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.free is not None:
                            return True

                        if self.lower_bound is not None:
                            return True

                        if self.size is not None:
                            return True

                        if self.upper_bound is not None:
                            return True

                        if self.used is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Srgb.State']['meta_info']

                @property
                def _common_path(self):
                    if self.lower_bound is None:
                        raise YPYDataValidationError('Key property lower_bound is None')
                    if self.upper_bound is None:
                        raise YPYDataValidationError('Key property upper_bound is None')

                    return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:segment-routing/openconfig-mpls:srgb[openconfig-mpls:lower-bound = ' + str(self.lower_bound) + '][openconfig-mpls:upper-bound = ' + str(self.upper_bound) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.lower_bound is not None:
                        return True

                    if self.upper_bound is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.config is not None and self.config.is_presence():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting.Srgb']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols/openconfig-mpls:segment-routing'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.interfaces is not None:
                    for child_ref in self.interfaces:
                        if child_ref._has_data():
                            return True

                if self.srgb is not None:
                    for child_ref in self.srgb:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.SignalingProtocols.SegmentRouting']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-mpls:mpls/openconfig-mpls:signaling-protocols'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ldp is not None and self.ldp._has_data():
                return True

            if self.ldp is not None and self.ldp.is_presence():
                return True

            if self.rsvp_te is not None and self.rsvp_te._has_data():
                return True

            if self.rsvp_te is not None and self.rsvp_te.is_presence():
                return True

            if self.segment_routing is not None and self.segment_routing._has_data():
                return True

            if self.segment_routing is not None and self.segment_routing.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_mpls as meta
            return meta._meta_table['Mpls.SignalingProtocols']['meta_info']


    class TeGlobalAttributes(object):
        """
        traffic\-engineering global attributes
        
        .. attribute:: igp_flooding_bandwidth
        
        	Interface bandwidth change percentages that trigger update events into the IGP traffic engineering database (TED)
        	**type**\: :py:class:`IgpFloodingBandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth>`
        
        .. attribute:: mpls_admin_groups
        
        	Top\-level container for admin\-groups configuration and state
        	**type**\: :py:class:`MplsAdminGroups <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups>`
        
        .. attribute:: srlg
        
        	Shared risk link groups attributes
        	**type**\: :py:class:`Srlg <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg>`
        
        .. attribute:: te_lsp_timers
        
        	Definition for delays associated with setup and cleanup of TE LSPs
        	**type**\: :py:class:`TeLspTimers <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.TeLspTimers>`
        
        

        """

        _prefix = 'mpls'
        _revision = '2015-11-05'

        def __init__(self):
            self.parent = None
            self.igp_flooding_bandwidth = Mpls.TeGlobalAttributes.IgpFloodingBandwidth()
            self.igp_flooding_bandwidth.parent = self
            self.mpls_admin_groups = Mpls.TeGlobalAttributes.MplsAdminGroups()
            self.mpls_admin_groups.parent = self
            self.srlg = Mpls.TeGlobalAttributes.Srlg()
            self.srlg.parent = self
            self.te_lsp_timers = Mpls.TeGlobalAttributes.TeLspTimers()
            self.te_lsp_timers.parent = self


        class IgpFloodingBandwidth(object):
            """
            Interface bandwidth change percentages
            that trigger update events into the IGP traffic
            engineering database (TED)
            
            .. attribute:: config
            
            	Configuration parameters for TED update threshold 
            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config>`
            
            .. attribute:: state
            
            	State parameters for TED update threshold 
            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.config = Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config()
                self.config.parent = self
                self.state = Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration parameters for TED
                update threshold 
                
                .. attribute:: delta_percentage
                
                	The percentage of the maximum\-reservable\-bandwidth considered as the delta that results in an IGP update being flooded
                	**type**\: int
                
                	**range:** 0..100
                
                .. attribute:: down_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is decreasing
                	**type**\: list of int
                
                	**range:** 0..100
                
                .. attribute:: threshold_specification
                
                	This value specifies whether a single set of threshold values should be used for both increasing and decreasing bandwidth when determining whether to trigger updated bandwidth values to be flooded in the IGP TE extensions. MIRRORED\-UP\-DOWN indicates that a single value (or set of values) should be used for both increasing and decreasing values, where SEPARATE\-UP\-DOWN specifies that the increasing and decreasing values will be separately specified
                	**type**\: :py:class:`ThresholdSpecification_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.ThresholdSpecification_Enum>`
                
                .. attribute:: threshold_type
                
                	The type of threshold that should be used to specify the values at which bandwidth is flooded. DELTA indicates that the local system should flood IGP updates when a change in reserved bandwidth >= the specified delta occurs on the interface. Where THRESHOLD\-CROSSED is specified, the local system should trigger an update (and hence flood) the reserved bandwidth when the reserved bandwidth changes such that it crosses, or becomes equal to one of the threshold values
                	**type**\: :py:class:`ThresholdType_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.ThresholdType_Enum>`
                
                .. attribute:: up_down_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth of the interface) at which bandwidth updates are flooded \- used both when the bandwidth is increasing and decreasing
                	**type**\: list of int
                
                	**range:** 0..100
                
                .. attribute:: up_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is increasing
                	**type**\: list of int
                
                	**range:** 0..100
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.delta_percentage = None
                    self.down_thresholds = []
                    self.threshold_specification = None
                    self.threshold_type = None
                    self.up_down_thresholds = []
                    self.up_thresholds = []

                class ThresholdSpecification_Enum(Enum):
                    """
                    ThresholdSpecification_Enum

                    This value specifies whether a single set of threshold
                    values should be used for both increasing and decreasing
                    bandwidth when determining whether to trigger updated
                    bandwidth values to be flooded in the IGP TE extensions.
                    MIRRORED\-UP\-DOWN indicates that a single value (or set of
                    values) should be used for both increasing and decreasing
                    values, where SEPARATE\-UP\-DOWN specifies that the increasing
                    and decreasing values will be separately specified

                    """

                    """

                    MIRRORED\-UP\-DOWN indicates that a single set of
                    threshold values should be used for both increasing
                    and decreasing bandwidth when determining whether
                    to trigger updated bandwidth values to be flooded
                    in the IGP TE extensions.

                    """
                    MIRRORED_UP_DOWN = 0

                    """

                    SEPARATE\-UP\-DOWN indicates that a separate
                    threshold values should be used for the increasing
                    and decreasing bandwidth when determining whether
                    to trigger updated bandwidth values to be flooded
                    in the IGP TE extensions.

                    """
                    SEPARATE_UP_DOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.ThresholdSpecification_Enum']


                class ThresholdType_Enum(Enum):
                    """
                    ThresholdType_Enum

                    The type of threshold that should be used to specify the
                    values at which bandwidth is flooded. DELTA indicates that
                    the local system should flood IGP updates when a change in
                    reserved bandwidth >= the specified delta occurs on the
                    interface. Where THRESHOLD\-CROSSED is specified, the local
                    system should trigger an update (and hence flood) the
                    reserved bandwidth when the reserved bandwidth changes such
                    that it crosses, or becomes equal to one of the threshold
                    values

                    """

                    """

                    DELTA indicates that the local
                    system should flood IGP updates when a
                    change in reserved bandwidth >= the specified
                    delta occurs on the interface.

                    """
                    DELTA = 0

                    """

                    THRESHOLD\-CROSSED indicates that
                    the local system should trigger an update (and
                    hence flood) the reserved bandwidth when the
                    reserved bandwidth changes such that it crosses,
                    or becomes equal to one of the threshold values.

                    """
                    THRESHOLD_CROSSED = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.ThresholdType_Enum']


                @property
                def _common_path(self):

                    return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes/openconfig-mpls:igp-flooding-bandwidth/openconfig-mpls:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.delta_percentage is not None:
                        return True

                    if self.down_thresholds is not None:
                        for child in self.down_thresholds:
                            if child is not None:
                                return True

                    if self.threshold_specification is not None:
                        return True

                    if self.threshold_type is not None:
                        return True

                    if self.up_down_thresholds is not None:
                        for child in self.up_down_thresholds:
                            if child is not None:
                                return True

                    if self.up_thresholds is not None:
                        for child in self.up_thresholds:
                            if child is not None:
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config']['meta_info']


            class State(object):
                """
                State parameters for TED update threshold 
                
                .. attribute:: delta_percentage
                
                	The percentage of the maximum\-reservable\-bandwidth considered as the delta that results in an IGP update being flooded
                	**type**\: int
                
                	**range:** 0..100
                
                .. attribute:: down_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is decreasing
                	**type**\: list of int
                
                	**range:** 0..100
                
                .. attribute:: threshold_specification
                
                	This value specifies whether a single set of threshold values should be used for both increasing and decreasing bandwidth when determining whether to trigger updated bandwidth values to be flooded in the IGP TE extensions. MIRRORED\-UP\-DOWN indicates that a single value (or set of values) should be used for both increasing and decreasing values, where SEPARATE\-UP\-DOWN specifies that the increasing and decreasing values will be separately specified
                	**type**\: :py:class:`ThresholdSpecification_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.ThresholdSpecification_Enum>`
                
                .. attribute:: threshold_type
                
                	The type of threshold that should be used to specify the values at which bandwidth is flooded. DELTA indicates that the local system should flood IGP updates when a change in reserved bandwidth >= the specified delta occurs on the interface. Where THRESHOLD\-CROSSED is specified, the local system should trigger an update (and hence flood) the reserved bandwidth when the reserved bandwidth changes such that it crosses, or becomes equal to one of the threshold values
                	**type**\: :py:class:`ThresholdType_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.ThresholdType_Enum>`
                
                .. attribute:: up_down_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth of the interface) at which bandwidth updates are flooded \- used both when the bandwidth is increasing and decreasing
                	**type**\: list of int
                
                	**range:** 0..100
                
                .. attribute:: up_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is increasing
                	**type**\: list of int
                
                	**range:** 0..100
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.delta_percentage = None
                    self.down_thresholds = []
                    self.threshold_specification = None
                    self.threshold_type = None
                    self.up_down_thresholds = []
                    self.up_thresholds = []

                class ThresholdSpecification_Enum(Enum):
                    """
                    ThresholdSpecification_Enum

                    This value specifies whether a single set of threshold
                    values should be used for both increasing and decreasing
                    bandwidth when determining whether to trigger updated
                    bandwidth values to be flooded in the IGP TE extensions.
                    MIRRORED\-UP\-DOWN indicates that a single value (or set of
                    values) should be used for both increasing and decreasing
                    values, where SEPARATE\-UP\-DOWN specifies that the increasing
                    and decreasing values will be separately specified

                    """

                    """

                    MIRRORED\-UP\-DOWN indicates that a single set of
                    threshold values should be used for both increasing
                    and decreasing bandwidth when determining whether
                    to trigger updated bandwidth values to be flooded
                    in the IGP TE extensions.

                    """
                    MIRRORED_UP_DOWN = 0

                    """

                    SEPARATE\-UP\-DOWN indicates that a separate
                    threshold values should be used for the increasing
                    and decreasing bandwidth when determining whether
                    to trigger updated bandwidth values to be flooded
                    in the IGP TE extensions.

                    """
                    SEPARATE_UP_DOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.ThresholdSpecification_Enum']


                class ThresholdType_Enum(Enum):
                    """
                    ThresholdType_Enum

                    The type of threshold that should be used to specify the
                    values at which bandwidth is flooded. DELTA indicates that
                    the local system should flood IGP updates when a change in
                    reserved bandwidth >= the specified delta occurs on the
                    interface. Where THRESHOLD\-CROSSED is specified, the local
                    system should trigger an update (and hence flood) the
                    reserved bandwidth when the reserved bandwidth changes such
                    that it crosses, or becomes equal to one of the threshold
                    values

                    """

                    """

                    DELTA indicates that the local
                    system should flood IGP updates when a
                    change in reserved bandwidth >= the specified
                    delta occurs on the interface.

                    """
                    DELTA = 0

                    """

                    THRESHOLD\-CROSSED indicates that
                    the local system should trigger an update (and
                    hence flood) the reserved bandwidth when the
                    reserved bandwidth changes such that it crosses,
                    or becomes equal to one of the threshold values.

                    """
                    THRESHOLD_CROSSED = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.ThresholdType_Enum']


                @property
                def _common_path(self):

                    return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes/openconfig-mpls:igp-flooding-bandwidth/openconfig-mpls:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.delta_percentage is not None:
                        return True

                    if self.down_thresholds is not None:
                        for child in self.down_thresholds:
                            if child is not None:
                                return True

                    if self.threshold_specification is not None:
                        return True

                    if self.threshold_type is not None:
                        return True

                    if self.up_down_thresholds is not None:
                        for child in self.up_down_thresholds:
                            if child is not None:
                                return True

                    if self.up_thresholds is not None:
                        for child in self.up_thresholds:
                            if child is not None:
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes/openconfig-mpls:igp-flooding-bandwidth'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.config is not None and self.config._has_data():
                    return True

                if self.config is not None and self.config.is_presence():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.state is not None and self.state.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth']['meta_info']


        class MplsAdminGroups(object):
            """
            Top\-level container for admin\-groups configuration
            and state
            
            .. attribute:: admin_group
            
            	configuration of value to name mapping for mpls affinities/admin\-groups
            	**type**\: list of :py:class:`AdminGroup <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.admin_group = YList()
                self.admin_group.parent = self
                self.admin_group.name = 'admin_group'


            class AdminGroup(object):
                """
                configuration of value to name mapping
                for mpls affinities/admin\-groups
                
                .. attribute:: admin_group_name
                
                	name for mpls admin\-group
                	**type**\: str
                
                .. attribute:: config
                
                	Configurable items for admin\-groups
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config>`
                
                .. attribute:: state
                
                	Operational state for admin\-groups
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.admin_group_name = None
                    self.config = Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config()
                    self.config.parent = self
                    self.state = Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configurable items for admin\-groups
                    
                    .. attribute:: admin_group_name
                    
                    	name for mpls admin\-group
                    	**type**\: str
                    
                    .. attribute:: bit_position
                    
                    	bit\-position value for mpls admin\-group. The value for the admin group is an integer that represents one of the bit positions in the admin\-group bitmask. Values between 0 and 31 are interpreted as the original limit of 32 admin groups. Values >=32 are interpreted as extended admin group values as per RFC7308
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.admin_group_name = None
                        self.bit_position = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.admin_group_name is not None:
                            return True

                        if self.bit_position is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config']['meta_info']


                class State(object):
                    """
                    Operational state for admin\-groups
                    
                    .. attribute:: admin_group_name
                    
                    	name for mpls admin\-group
                    	**type**\: str
                    
                    .. attribute:: bit_position
                    
                    	bit\-position value for mpls admin\-group. The value for the admin group is an integer that represents one of the bit positions in the admin\-group bitmask. Values between 0 and 31 are interpreted as the original limit of 32 admin groups. Values >=32 are interpreted as extended admin group values as per RFC7308
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.admin_group_name = None
                        self.bit_position = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.admin_group_name is not None:
                            return True

                        if self.bit_position is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State']['meta_info']

                @property
                def _common_path(self):
                    if self.admin_group_name is None:
                        raise YPYDataValidationError('Key property admin_group_name is None')

                    return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes/openconfig-mpls:mpls-admin-groups/openconfig-mpls:admin-group[openconfig-mpls:admin-group-name = ' + str(self.admin_group_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.admin_group_name is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.config is not None and self.config.is_presence():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes/openconfig-mpls:mpls-admin-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.admin_group is not None:
                    for child_ref in self.admin_group:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups']['meta_info']


        class Srlg(object):
            """
            Shared risk link groups attributes
            
            .. attribute:: srlg
            
            	List of shared risk link groups
            	**type**\: list of :py:class:`Srlg <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.srlg = YList()
                self.srlg.parent = self
                self.srlg.name = 'srlg'


            class Srlg(object):
                """
                List of shared risk link groups
                
                .. attribute:: name
                
                	The SRLG group identifier
                	**type**\: str
                
                .. attribute:: config
                
                	Configuration parameters related to the SRLG
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.Config>`
                
                .. attribute:: state
                
                	State parameters related to the SRLG
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.State>`
                
                .. attribute:: static_srlg_members
                
                	SRLG members for static (not flooded) SRLGs 
                	**type**\: :py:class:`StaticSrlgMembers <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.config = Mpls.TeGlobalAttributes.Srlg.Srlg.Config()
                    self.config.parent = self
                    self.state = Mpls.TeGlobalAttributes.Srlg.Srlg.State()
                    self.state.parent = self
                    self.static_srlg_members = Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers()
                    self.static_srlg_members.parent = self


                class Config(object):
                    """
                    Configuration parameters related to the SRLG
                    
                    .. attribute:: cost
                    
                    	The cost of the SRLG to the computation algorithm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flooding_type
                    
                    	The type of SRLG, either flooded in the IGP or statically configured
                    	**type**\: :py:class:`MplsSrlgFloodingType_Enum <ydk.models.openconfig.openconfig_mpls.MplsSrlgFloodingType_Enum>`
                    
                    .. attribute:: name
                    
                    	SRLG group identifier
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	group ID for the SRLG
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.cost = None
                        self.flooding_type = None
                        self.name = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.cost is not None:
                            return True

                        if self.flooding_type is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg.Config']['meta_info']


                class State(object):
                    """
                    State parameters related to the SRLG
                    
                    .. attribute:: cost
                    
                    	The cost of the SRLG to the computation algorithm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flooding_type
                    
                    	The type of SRLG, either flooded in the IGP or statically configured
                    	**type**\: :py:class:`MplsSrlgFloodingType_Enum <ydk.models.openconfig.openconfig_mpls.MplsSrlgFloodingType_Enum>`
                    
                    .. attribute:: name
                    
                    	SRLG group identifier
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	group ID for the SRLG
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.cost = None
                        self.flooding_type = None
                        self.name = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.cost is not None:
                            return True

                        if self.flooding_type is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg.State']['meta_info']


                class StaticSrlgMembers(object):
                    """
                    SRLG members for static (not flooded) SRLGs 
                    
                    .. attribute:: members_list
                    
                    	List of SRLG members, which are expressed as IP address endpoints of links contained in the SRLG
                    	**type**\: list of :py:class:`MembersList <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.members_list = YList()
                        self.members_list.parent = self
                        self.members_list.name = 'members_list'


                    class MembersList(object):
                        """
                        List of SRLG members, which are expressed
                        as IP address endpoints of links contained in the
                        SRLG
                        
                        .. attribute:: from_address
                        
                        	The from address of the link in the SRLG
                        	**type**\: one of { str | str }
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the SRLG members
                        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to the SRLG members
                        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            self.parent = None
                            self.from_address = None
                            self.config = Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.Config()
                            self.config.parent = self
                            self.state = Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration parameters relating to the
                            SRLG members
                            
                            .. attribute:: from_address
                            
                            	IP address of the a\-side of the SRLG link
                            	**type**\: one of { str | str }
                            
                            .. attribute:: to_address
                            
                            	IP address of the z\-side of the SRLG link
                            	**type**\: one of { str | str }
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.from_address = None
                                self.to_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.from_address is not None:
                                    return True

                                if self.to_address is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.Config']['meta_info']


                        class State(object):
                            """
                            State parameters relating to the SRLG
                            members
                            
                            .. attribute:: from_address
                            
                            	IP address of the a\-side of the SRLG link
                            	**type**\: one of { str | str }
                            
                            .. attribute:: to_address
                            
                            	IP address of the z\-side of the SRLG link
                            	**type**\: one of { str | str }
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                self.parent = None
                                self.from_address = None
                                self.to_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-mpls:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.from_address is not None:
                                    return True

                                if self.to_address is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                                return meta._meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.from_address is None:
                                raise YPYDataValidationError('Key property from_address is None')

                            return self.parent._common_path +'/openconfig-mpls:members-list[openconfig-mpls:from-address = ' + str(self.from_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.from_address is not None:
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.config is not None and self.config.is_presence():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.state is not None and self.state.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:static-srlg-members'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.members_list is not None:
                            for child_ref in self.members_list:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes/openconfig-mpls:srlg/openconfig-mpls:srlg[openconfig-mpls:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.config is not None and self.config.is_presence():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    if self.static_srlg_members is not None and self.static_srlg_members._has_data():
                        return True

                    if self.static_srlg_members is not None and self.static_srlg_members.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes/openconfig-mpls:srlg'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.srlg is not None:
                    for child_ref in self.srlg:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.TeGlobalAttributes.Srlg']['meta_info']


        class TeLspTimers(object):
            """
            Definition for delays associated with setup
            and cleanup of TE LSPs
            
            .. attribute:: config
            
            	Configuration parameters related to timers for TE LSPs
            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.TeLspTimers.Config>`
            
            .. attribute:: state
            
            	State related to timers for TE LSPs
            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.TeLspTimers.State>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.config = Mpls.TeGlobalAttributes.TeLspTimers.Config()
                self.config.parent = self
                self.state = Mpls.TeGlobalAttributes.TeLspTimers.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration parameters related
                to timers for TE LSPs
                
                .. attribute:: cleanup_delay
                
                	delay the removal of old te lsp for a specified amount of time
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: install_delay
                
                	delay the use of newly installed te lsp for a specified amount of time
                	**type**\: int
                
                	**range:** 0..3600
                
                .. attribute:: reoptimize_timer
                
                	frequency of reoptimization of a traffic engineered LSP
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.cleanup_delay = None
                    self.install_delay = None
                    self.reoptimize_timer = None

                @property
                def _common_path(self):

                    return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes/openconfig-mpls:te-lsp-timers/openconfig-mpls:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.cleanup_delay is not None:
                        return True

                    if self.install_delay is not None:
                        return True

                    if self.reoptimize_timer is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.TeGlobalAttributes.TeLspTimers.Config']['meta_info']


            class State(object):
                """
                State related to timers for TE LSPs
                
                .. attribute:: cleanup_delay
                
                	delay the removal of old te lsp for a specified amount of time
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: install_delay
                
                	delay the use of newly installed te lsp for a specified amount of time
                	**type**\: int
                
                	**range:** 0..3600
                
                .. attribute:: reoptimize_timer
                
                	frequency of reoptimization of a traffic engineered LSP
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.cleanup_delay = None
                    self.install_delay = None
                    self.reoptimize_timer = None

                @property
                def _common_path(self):

                    return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes/openconfig-mpls:te-lsp-timers/openconfig-mpls:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.cleanup_delay is not None:
                        return True

                    if self.install_delay is not None:
                        return True

                    if self.reoptimize_timer is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.TeGlobalAttributes.TeLspTimers.State']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes/openconfig-mpls:te-lsp-timers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.config is not None and self.config._has_data():
                    return True

                if self.config is not None and self.config.is_presence():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.state is not None and self.state.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.TeGlobalAttributes.TeLspTimers']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-mpls:mpls/openconfig-mpls:te-global-attributes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.igp_flooding_bandwidth is not None and self.igp_flooding_bandwidth._has_data():
                return True

            if self.igp_flooding_bandwidth is not None and self.igp_flooding_bandwidth.is_presence():
                return True

            if self.mpls_admin_groups is not None and self.mpls_admin_groups._has_data():
                return True

            if self.mpls_admin_groups is not None and self.mpls_admin_groups.is_presence():
                return True

            if self.srlg is not None and self.srlg._has_data():
                return True

            if self.srlg is not None and self.srlg.is_presence():
                return True

            if self.te_lsp_timers is not None and self.te_lsp_timers._has_data():
                return True

            if self.te_lsp_timers is not None and self.te_lsp_timers.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_mpls as meta
            return meta._meta_table['Mpls.TeGlobalAttributes']['meta_info']


    class TeInterfaceAttributes(object):
        """
        traffic engineering attributes specific
        for interfaces
        
        .. attribute:: interface
        
        	List of TE interfaces
        	**type**\: list of :py:class:`Interface <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface>`
        
        

        """

        _prefix = 'mpls'
        _revision = '2015-11-05'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            List of TE interfaces
            
            .. attribute:: name
            
            	The interface name
            	**type**\: str
            
            .. attribute:: config
            
            	Configuration parameters related to TE interfaces\:
            	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.Config>`
            
            .. attribute:: igp_flooding_bandwidth
            
            	Interface bandwidth change percentages that trigger update events into the IGP traffic engineering database (TED)
            	**type**\: :py:class:`IgpFloodingBandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth>`
            
            .. attribute:: state
            
            	State parameters related to TE interfaces
            	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.State>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                self.parent = None
                self.name = None
                self.config = Mpls.TeInterfaceAttributes.Interface.Config()
                self.config.parent = self
                self.igp_flooding_bandwidth = Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth()
                self.igp_flooding_bandwidth.parent = self
                self.state = Mpls.TeInterfaceAttributes.Interface.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration parameters related to TE interfaces\:
                
                .. attribute:: admin_group
                
                	list of admin groups (by name) on the interface
                	**type**\: list of str
                
                .. attribute:: name
                
                	reference to interface name
                	**type**\: str
                
                .. attribute:: srlg_membership
                
                	list of references to named shared risk link groups that the interface belongs to
                	**type**\: list of str
                
                .. attribute:: te_metric
                
                	TE specific metric for the link
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.admin_group = []
                    self.name = None
                    self.srlg_membership = []
                    self.te_metric = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-mpls:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.admin_group is not None:
                        for child in self.admin_group:
                            if child is not None:
                                return True

                    if self.name is not None:
                        return True

                    if self.srlg_membership is not None:
                        for child in self.srlg_membership:
                            if child is not None:
                                return True

                    if self.te_metric is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.TeInterfaceAttributes.Interface.Config']['meta_info']


            class IgpFloodingBandwidth(object):
                """
                Interface bandwidth change percentages
                that trigger update events into the IGP traffic
                engineering database (TED)
                
                .. attribute:: config
                
                	Configuration parameters for TED update threshold 
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config>`
                
                .. attribute:: state
                
                	State parameters for TED update threshold 
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.config = Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config()
                    self.config.parent = self
                    self.state = Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters for TED
                    update threshold 
                    
                    .. attribute:: delta_percentage
                    
                    	The percentage of the maximum\-reservable\-bandwidth considered as the delta that results in an IGP update being flooded
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    .. attribute:: down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is decreasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    .. attribute:: threshold_specification
                    
                    	This value specifies whether a single set of threshold values should be used for both increasing and decreasing bandwidth when determining whether to trigger updated bandwidth values to be flooded in the IGP TE extensions. MIRRORED\-UP\-DOWN indicates that a single value (or set of values) should be used for both increasing and decreasing values, where SEPARATE\-UP\-DOWN specifies that the increasing and decreasing values will be separately specified
                    	**type**\: :py:class:`ThresholdSpecification_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdSpecification_Enum>`
                    
                    .. attribute:: threshold_type
                    
                    	The type of threshold that should be used to specify the values at which bandwidth is flooded. DELTA indicates that the local system should flood IGP updates when a change in reserved bandwidth >= the specified delta occurs on the interface. Where THRESHOLD\-CROSSED is specified, the local system should trigger an update (and hence flood) the reserved bandwidth when the reserved bandwidth changes such that it crosses, or becomes equal to one of the threshold values
                    	**type**\: :py:class:`ThresholdType_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdType_Enum>`
                    
                    .. attribute:: up_down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth of the interface) at which bandwidth updates are flooded \- used both when the bandwidth is increasing and decreasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    .. attribute:: up_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is increasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.delta_percentage = None
                        self.down_thresholds = []
                        self.threshold_specification = None
                        self.threshold_type = None
                        self.up_down_thresholds = []
                        self.up_thresholds = []

                    class ThresholdSpecification_Enum(Enum):
                        """
                        ThresholdSpecification_Enum

                        This value specifies whether a single set of threshold
                        values should be used for both increasing and decreasing
                        bandwidth when determining whether to trigger updated
                        bandwidth values to be flooded in the IGP TE extensions.
                        MIRRORED\-UP\-DOWN indicates that a single value (or set of
                        values) should be used for both increasing and decreasing
                        values, where SEPARATE\-UP\-DOWN specifies that the increasing
                        and decreasing values will be separately specified

                        """

                        """

                        MIRRORED\-UP\-DOWN indicates that a single set of
                        threshold values should be used for both increasing
                        and decreasing bandwidth when determining whether
                        to trigger updated bandwidth values to be flooded
                        in the IGP TE extensions.

                        """
                        MIRRORED_UP_DOWN = 0

                        """

                        SEPARATE\-UP\-DOWN indicates that a separate
                        threshold values should be used for the increasing
                        and decreasing bandwidth when determining whether
                        to trigger updated bandwidth values to be flooded
                        in the IGP TE extensions.

                        """
                        SEPARATE_UP_DOWN = 1


                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdSpecification_Enum']


                    class ThresholdType_Enum(Enum):
                        """
                        ThresholdType_Enum

                        The type of threshold that should be used to specify the
                        values at which bandwidth is flooded. DELTA indicates that
                        the local system should flood IGP updates when a change in
                        reserved bandwidth >= the specified delta occurs on the
                        interface. Where THRESHOLD\-CROSSED is specified, the local
                        system should trigger an update (and hence flood) the
                        reserved bandwidth when the reserved bandwidth changes such
                        that it crosses, or becomes equal to one of the threshold
                        values

                        """

                        """

                        DELTA indicates that the local
                        system should flood IGP updates when a
                        change in reserved bandwidth >= the specified
                        delta occurs on the interface.

                        """
                        DELTA = 0

                        """

                        THRESHOLD\-CROSSED indicates that
                        the local system should trigger an update (and
                        hence flood) the reserved bandwidth when the
                        reserved bandwidth changes such that it crosses,
                        or becomes equal to one of the threshold values.

                        """
                        THRESHOLD_CROSSED = 1


                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdType_Enum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.delta_percentage is not None:
                            return True

                        if self.down_thresholds is not None:
                            for child in self.down_thresholds:
                                if child is not None:
                                    return True

                        if self.threshold_specification is not None:
                            return True

                        if self.threshold_type is not None:
                            return True

                        if self.up_down_thresholds is not None:
                            for child in self.up_down_thresholds:
                                if child is not None:
                                    return True

                        if self.up_thresholds is not None:
                            for child in self.up_thresholds:
                                if child is not None:
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config']['meta_info']


                class State(object):
                    """
                    State parameters for TED update threshold 
                    
                    .. attribute:: delta_percentage
                    
                    	The percentage of the maximum\-reservable\-bandwidth considered as the delta that results in an IGP update being flooded
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    .. attribute:: down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is decreasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    .. attribute:: threshold_specification
                    
                    	This value specifies whether a single set of threshold values should be used for both increasing and decreasing bandwidth when determining whether to trigger updated bandwidth values to be flooded in the IGP TE extensions. MIRRORED\-UP\-DOWN indicates that a single value (or set of values) should be used for both increasing and decreasing values, where SEPARATE\-UP\-DOWN specifies that the increasing and decreasing values will be separately specified
                    	**type**\: :py:class:`ThresholdSpecification_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdSpecification_Enum>`
                    
                    .. attribute:: threshold_type
                    
                    	The type of threshold that should be used to specify the values at which bandwidth is flooded. DELTA indicates that the local system should flood IGP updates when a change in reserved bandwidth >= the specified delta occurs on the interface. Where THRESHOLD\-CROSSED is specified, the local system should trigger an update (and hence flood) the reserved bandwidth when the reserved bandwidth changes such that it crosses, or becomes equal to one of the threshold values
                    	**type**\: :py:class:`ThresholdType_Enum <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdType_Enum>`
                    
                    .. attribute:: up_down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth of the interface) at which bandwidth updates are flooded \- used both when the bandwidth is increasing and decreasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    .. attribute:: up_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is increasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        self.parent = None
                        self.delta_percentage = None
                        self.down_thresholds = []
                        self.threshold_specification = None
                        self.threshold_type = None
                        self.up_down_thresholds = []
                        self.up_thresholds = []

                    class ThresholdSpecification_Enum(Enum):
                        """
                        ThresholdSpecification_Enum

                        This value specifies whether a single set of threshold
                        values should be used for both increasing and decreasing
                        bandwidth when determining whether to trigger updated
                        bandwidth values to be flooded in the IGP TE extensions.
                        MIRRORED\-UP\-DOWN indicates that a single value (or set of
                        values) should be used for both increasing and decreasing
                        values, where SEPARATE\-UP\-DOWN specifies that the increasing
                        and decreasing values will be separately specified

                        """

                        """

                        MIRRORED\-UP\-DOWN indicates that a single set of
                        threshold values should be used for both increasing
                        and decreasing bandwidth when determining whether
                        to trigger updated bandwidth values to be flooded
                        in the IGP TE extensions.

                        """
                        MIRRORED_UP_DOWN = 0

                        """

                        SEPARATE\-UP\-DOWN indicates that a separate
                        threshold values should be used for the increasing
                        and decreasing bandwidth when determining whether
                        to trigger updated bandwidth values to be flooded
                        in the IGP TE extensions.

                        """
                        SEPARATE_UP_DOWN = 1


                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdSpecification_Enum']


                    class ThresholdType_Enum(Enum):
                        """
                        ThresholdType_Enum

                        The type of threshold that should be used to specify the
                        values at which bandwidth is flooded. DELTA indicates that
                        the local system should flood IGP updates when a change in
                        reserved bandwidth >= the specified delta occurs on the
                        interface. Where THRESHOLD\-CROSSED is specified, the local
                        system should trigger an update (and hence flood) the
                        reserved bandwidth when the reserved bandwidth changes such
                        that it crosses, or becomes equal to one of the threshold
                        values

                        """

                        """

                        DELTA indicates that the local
                        system should flood IGP updates when a
                        change in reserved bandwidth >= the specified
                        delta occurs on the interface.

                        """
                        DELTA = 0

                        """

                        THRESHOLD\-CROSSED indicates that
                        the local system should trigger an update (and
                        hence flood) the reserved bandwidth when the
                        reserved bandwidth changes such that it crosses,
                        or becomes equal to one of the threshold values.

                        """
                        THRESHOLD_CROSSED = 1


                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_mpls as meta
                            return meta._meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdType_Enum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-mpls:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.delta_percentage is not None:
                            return True

                        if self.down_thresholds is not None:
                            for child in self.down_thresholds:
                                if child is not None:
                                    return True

                        if self.threshold_specification is not None:
                            return True

                        if self.threshold_type is not None:
                            return True

                        if self.up_down_thresholds is not None:
                            for child in self.up_down_thresholds:
                                if child is not None:
                                    return True

                        if self.up_thresholds is not None:
                            for child in self.up_thresholds:
                                if child is not None:
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_mpls as meta
                        return meta._meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-mpls:igp-flooding-bandwidth'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.config is not None and self.config.is_presence():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.state is not None and self.state.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth']['meta_info']


            class State(object):
                """
                State parameters related to TE interfaces
                
                .. attribute:: admin_group
                
                	list of admin groups (by name) on the interface
                	**type**\: list of str
                
                .. attribute:: name
                
                	reference to interface name
                	**type**\: str
                
                .. attribute:: srlg_membership
                
                	list of references to named shared risk link groups that the interface belongs to
                	**type**\: list of str
                
                .. attribute:: te_metric
                
                	TE specific metric for the link
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    self.parent = None
                    self.admin_group = []
                    self.name = None
                    self.srlg_membership = []
                    self.te_metric = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-mpls:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.admin_group is not None:
                        for child in self.admin_group:
                            if child is not None:
                                return True

                    if self.name is not None:
                        return True

                    if self.srlg_membership is not None:
                        for child in self.srlg_membership:
                            if child is not None:
                                return True

                    if self.te_metric is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_mpls as meta
                    return meta._meta_table['Mpls.TeInterfaceAttributes.Interface.State']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/openconfig-mpls:mpls/openconfig-mpls:te-interface-attributes/openconfig-mpls:interface[openconfig-mpls:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.name is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.config is not None and self.config.is_presence():
                    return True

                if self.igp_flooding_bandwidth is not None and self.igp_flooding_bandwidth._has_data():
                    return True

                if self.igp_flooding_bandwidth is not None and self.igp_flooding_bandwidth.is_presence():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.state is not None and self.state.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_mpls as meta
                return meta._meta_table['Mpls.TeInterfaceAttributes.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-mpls:mpls/openconfig-mpls:te-interface-attributes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_mpls as meta
            return meta._meta_table['Mpls.TeInterfaceAttributes']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-mpls:mpls'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.global_ is not None and self.global_._has_data():
            return True

        if self.global_ is not None and self.global_.is_presence():
            return True

        if self.lsps is not None and self.lsps._has_data():
            return True

        if self.lsps is not None and self.lsps.is_presence():
            return True

        if self.signaling_protocols is not None and self.signaling_protocols._has_data():
            return True

        if self.signaling_protocols is not None and self.signaling_protocols.is_presence():
            return True

        if self.te_global_attributes is not None and self.te_global_attributes._has_data():
            return True

        if self.te_global_attributes is not None and self.te_global_attributes.is_presence():
            return True

        if self.te_interface_attributes is not None and self.te_interface_attributes._has_data():
            return True

        if self.te_interface_attributes is not None and self.te_interface_attributes.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return True

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls as meta
        return meta._meta_table['Mpls']['meta_info']


class PathComputationMethod_Identity(object):
    """
    base identity for supported path computation
    mechanisms
    
    

    """

    _prefix = 'mpls'
    _revision = '2015-11-05'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls as meta
        return meta._meta_table['PathComputationMethod_Identity']['meta_info']


class ExplicitlyDefined_Identity(PathComputationMethod_Identity):
    """
    constrained\-path LSP in which the path is
    explicitly specified as a collection of strict or/and loose
    hops
    
    

    """

    _prefix = 'mpls'
    _revision = '2015-11-05'

    def __init__(self):
        PathComputationMethod_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls as meta
        return meta._meta_table['ExplicitlyDefined_Identity']['meta_info']


class ExternallyQueried_Identity(PathComputationMethod_Identity):
    """
    constrained\-path LSP in which the path is
    obtained by querying an external source, such as a PCE server
    
    

    """

    _prefix = 'mpls'
    _revision = '2015-11-05'

    def __init__(self):
        PathComputationMethod_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls as meta
        return meta._meta_table['ExternallyQueried_Identity']['meta_info']


class LocallyComputed_Identity(PathComputationMethod_Identity):
    """
    indicates a constrained\-path LSP in which the
    path is computed by the local LER
    
    

    """

    _prefix = 'mpls'
    _revision = '2015-11-05'

    def __init__(self):
        PathComputationMethod_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls as meta
        return meta._meta_table['LocallyComputed_Identity']['meta_info']

