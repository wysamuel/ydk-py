""" Cisco_IOS_XR_config_mda_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-mda package configuration.

This module contains definitions
for the following management objects\:
  active\-nodes\: Per\-node configuration for active nodes
  preconfigured\-nodes\: preconfigured nodes

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg import LptsFlow_Enum


class ActiveNodes(object):
    """
    Per\-node configuration for active nodes
    
    .. attribute:: active_node
    
    	The configuration for an active node
    	**type**\: list of :py:class:`ActiveNode <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode>`
    
    

    """

    _prefix = 'config-mda-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.active_node = YList()
        self.active_node.parent = self
        self.active_node.name = 'active_node'


    class ActiveNode(object):
        """
        The configuration for an active node
        
        .. attribute:: node_name
        
        	The identifier for this node
        	**type**\: str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: cisco_ios_xr_watchd_cfg_watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\: :py:class:`CiscoIOSXRWatchdCfg_watchdogNodeThreshold <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold>`
        
        .. attribute:: cisco_ios_xr_wd_cfg_watchdog_node_threshold
        
        	Watchdog threshold configuration
        	**type**\: :py:class:`CiscoIOSXRWdCfg_watchdogNodeThreshold <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\: :py:class:`LptsLocal <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node_name = None
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold()
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold()
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
            self.lpts_local = ActiveNodes.ActiveNode.LptsLocal()
            self.lpts_local.parent = self


        class CiscoIOSXRWatchdCfg_watchdogNodeThreshold(object):
            """
            watchdog node threshold
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\: :py:class:`MemoryThreshold <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.memory_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self


            class MemoryThreshold(object):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.critical = None
                    self.minor = None
                    self.severe = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-watchd-cfg:memory-threshold'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.critical is not None:
                        return True

                    if self.minor is not None:
                        return True

                    if self.severe is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-watchd-cfg:Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.memory_threshold is not None and self.memory_threshold._has_data():
                    return True

                if self.memory_threshold is not None and self.memory_threshold.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold']['meta_info']


        class CiscoIOSXRWdCfg_watchdogNodeThreshold(object):
            """
            Watchdog threshold configuration
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\: :py:class:`MemoryThreshold <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'wd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.memory_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self


            class MemoryThreshold(object):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'wd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.critical = None
                    self.minor = None
                    self.severe = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-wd-cfg:memory-threshold'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.critical is not None:
                        return True

                    if self.minor is not None:
                        return True

                    if self.severe is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-wd-cfg:Cisco-IOS-XR-wd-cfg_watchdog-node-threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.memory_threshold is not None and self.memory_threshold._has_data():
                    return True

                if self.memory_threshold is not None and self.memory_threshold.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold']['meta_info']


        class LptsLocal(object):
            """
            lpts node specific configuration commands
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\: :py:class:`IpolicerLocal <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal>`
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\: :py:class:`IpolicerLocalTables <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ipolicer_local = None
                self.ipolicer_local_tables = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self


            class IpolicerLocal(object):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\: :py:class:`Flows <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.flows = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self


                class Flows(object):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of :py:class:`Flow <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.flow = YList()
                        self.flow.parent = self
                        self.flow.name = 'flow'


                    class Flow(object):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type
                        
                        	LPTS Flow Type
                        	**type**\: :py:class:`LptsFlow_Enum <ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow_Enum>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\: :py:class:`Precedences <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.flow_type = None
                            self.precedences = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self.rate = None


                        class Precedences(object):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: list of one of { list of :py:class:`LptsPreIFibPrecedenceNumber_Enum <ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber_Enum>` | list of int }
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.precedence = []

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:precedences'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.precedence is not None:
                                    for child in self.precedence:
                                        if child is not None:
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.flow_type is None:
                                raise YPYDataValidationError('Key property flow_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:flow[Cisco-IOS-XR-lpts-pre-ifib-cfg:flow-type = ' + str(self.flow_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.flow_type is not None:
                                return True

                            if self.precedences is not None and self.precedences._has_data():
                                return True

                            if self.precedences is not None and self.precedences.is_presence():
                                return True

                            if self.rate is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:flows'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.flow is not None:
                            for child_ref in self.flow:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local'

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

                    if self.flows is not None and self.flows._has_data():
                        return True

                    if self.flows is not None and self.flows.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return True

                @staticmethod
                def _meta_info():
                    from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal']['meta_info']


            class IpolicerLocalTables(object):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of :py:class:`IpolicerLocalTable <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipolicer_local_table = YList()
                    self.ipolicer_local_table.parent = self
                    self.ipolicer_local_table.name = 'ipolicer_local_table'


                class IpolicerLocalTable(object):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1
                    
                    	none
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: nps
                    
                    	NP name
                    	**type**\: :py:class:`Nps <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.id1 = None
                        self.nps = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps()
                        self.nps.parent = self


                    class Nps(object):
                        """
                        NP name
                        
                        .. attribute:: np
                        
                        	Table of NP names
                        	**type**\: list of :py:class:`Np <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.np = YList()
                            self.np.parent = self
                            self.np.name = 'np'


                        class Np(object):
                            """
                            Table of NP names
                            
                            .. attribute:: id1
                            
                            	none
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate
                            
                            	Packets per second
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.id1 = None
                                self.rate = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.id1 is None:
                                    raise YPYDataValidationError('Key property id1 is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:np[Cisco-IOS-XR-lpts-pre-ifib-cfg:id1 = ' + str(self.id1) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.id1 is not None:
                                    return True

                                if self.rate is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:nps'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.np is not None:
                                for child_ref in self.np:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.id1 is None:
                            raise YPYDataValidationError('Key property id1 is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local-table[Cisco-IOS-XR-lpts-pre-ifib-cfg:id1 = ' + str(self.id1) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.id1 is not None:
                            return True

                        if self.nps is not None and self.nps._has_data():
                            return True

                        if self.nps is not None and self.nps.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local-tables'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ipolicer_local_table is not None:
                        for child_ref in self.ipolicer_local_table:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ipolicer_local is not None and self.ipolicer_local._has_data():
                    return True

                if self.ipolicer_local is not None and self.ipolicer_local.is_presence():
                    return True

                if self.ipolicer_local_tables is not None and self.ipolicer_local_tables._has_data():
                    return True

                if self.ipolicer_local_tables is not None and self.ipolicer_local_tables.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal']['meta_info']

        @property
        def _common_path(self):
            if self.node_name is None:
                raise YPYDataValidationError('Key property node_name is None')

            return '/Cisco-IOS-XR-config-mda-cfg:active-nodes/Cisco-IOS-XR-config-mda-cfg:active-node[Cisco-IOS-XR-config-mda-cfg:node-name = ' + str(self.node_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.node_name is not None:
                return True

            if self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold._has_data():
                return True

            if self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.is_presence():
                return True

            if self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_wd_cfg_watchdog_node_threshold._has_data():
                return True

            if self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.is_presence():
                return True

            if self.lpts_local is not None and self.lpts_local._has_data():
                return True

            if self.lpts_local is not None and self.lpts_local.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
            return meta._meta_table['ActiveNodes.ActiveNode']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-config-mda-cfg:active-nodes'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.active_node is not None:
            for child_ref in self.active_node:
                if child_ref._has_data():
                    return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
        return meta._meta_table['ActiveNodes']['meta_info']


class PreconfiguredNodes(object):
    """
    preconfigured nodes
    
    .. attribute:: preconfigured_node
    
    	The configuration for a non\-active node
    	**type**\: list of :py:class:`PreconfiguredNode <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode>`
    
    

    """

    _prefix = 'config-mda-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.preconfigured_node = YList()
        self.preconfigured_node.parent = self
        self.preconfigured_node.name = 'preconfigured_node'


    class PreconfiguredNode(object):
        """
        The configuration for a non\-active node
        
        .. attribute:: node_name
        
        	The identifier for this node
        	**type**\: str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: cisco_ios_xr_watchd_cfg_watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\: :py:class:`CiscoIOSXRWatchdCfg_watchdogNodeThreshold <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold>`
        
        .. attribute:: cisco_ios_xr_wd_cfg_watchdog_node_threshold
        
        	Watchdog threshold configuration
        	**type**\: :py:class:`CiscoIOSXRWdCfg_watchdogNodeThreshold <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\: :py:class:`LptsLocal <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node_name = None
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold()
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold()
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
            self.lpts_local = PreconfiguredNodes.PreconfiguredNode.LptsLocal()
            self.lpts_local.parent = self


        class CiscoIOSXRWatchdCfg_watchdogNodeThreshold(object):
            """
            watchdog node threshold
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\: :py:class:`MemoryThreshold <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self


            class MemoryThreshold(object):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.critical = None
                    self.minor = None
                    self.severe = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-watchd-cfg:memory-threshold'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.critical is not None:
                        return True

                    if self.minor is not None:
                        return True

                    if self.severe is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-watchd-cfg:Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.memory_threshold is not None and self.memory_threshold._has_data():
                    return True

                if self.memory_threshold is not None and self.memory_threshold.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold']['meta_info']


        class CiscoIOSXRWdCfg_watchdogNodeThreshold(object):
            """
            Watchdog threshold configuration
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\: :py:class:`MemoryThreshold <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'wd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self


            class MemoryThreshold(object):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'wd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.critical = None
                    self.minor = None
                    self.severe = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-wd-cfg:memory-threshold'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.critical is not None:
                        return True

                    if self.minor is not None:
                        return True

                    if self.severe is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-wd-cfg:Cisco-IOS-XR-wd-cfg_watchdog-node-threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.memory_threshold is not None and self.memory_threshold._has_data():
                    return True

                if self.memory_threshold is not None and self.memory_threshold.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold']['meta_info']


        class LptsLocal(object):
            """
            lpts node specific configuration commands
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\: :py:class:`IpolicerLocal <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal>`
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\: :py:class:`IpolicerLocalTables <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ipolicer_local = None
                self.ipolicer_local_tables = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self


            class IpolicerLocal(object):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\: :py:class:`Flows <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.flows = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self


                class Flows(object):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of :py:class:`Flow <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.flow = YList()
                        self.flow.parent = self
                        self.flow.name = 'flow'


                    class Flow(object):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type
                        
                        	LPTS Flow Type
                        	**type**\: :py:class:`LptsFlow_Enum <ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow_Enum>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\: :py:class:`Precedences <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.flow_type = None
                            self.precedences = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self.rate = None


                        class Precedences(object):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: list of one of { list of :py:class:`LptsPreIFibPrecedenceNumber_Enum <ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber_Enum>` | list of int }
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.precedence = []

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:precedences'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.precedence is not None:
                                    for child in self.precedence:
                                        if child is not None:
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.flow_type is None:
                                raise YPYDataValidationError('Key property flow_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:flow[Cisco-IOS-XR-lpts-pre-ifib-cfg:flow-type = ' + str(self.flow_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.flow_type is not None:
                                return True

                            if self.precedences is not None and self.precedences._has_data():
                                return True

                            if self.precedences is not None and self.precedences.is_presence():
                                return True

                            if self.rate is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:flows'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.flow is not None:
                            for child_ref in self.flow:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local'

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

                    if self.flows is not None and self.flows._has_data():
                        return True

                    if self.flows is not None and self.flows.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return True

                @staticmethod
                def _meta_info():
                    from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal']['meta_info']


            class IpolicerLocalTables(object):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of :py:class:`IpolicerLocalTable <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipolicer_local_table = YList()
                    self.ipolicer_local_table.parent = self
                    self.ipolicer_local_table.name = 'ipolicer_local_table'


                class IpolicerLocalTable(object):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1
                    
                    	none
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: nps
                    
                    	NP name
                    	**type**\: :py:class:`Nps <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.id1 = None
                        self.nps = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps()
                        self.nps.parent = self


                    class Nps(object):
                        """
                        NP name
                        
                        .. attribute:: np
                        
                        	Table of NP names
                        	**type**\: list of :py:class:`Np <ydk.models.config.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.np = YList()
                            self.np.parent = self
                            self.np.name = 'np'


                        class Np(object):
                            """
                            Table of NP names
                            
                            .. attribute:: id1
                            
                            	none
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate
                            
                            	Packets per second
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.id1 = None
                                self.rate = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.id1 is None:
                                    raise YPYDataValidationError('Key property id1 is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:np[Cisco-IOS-XR-lpts-pre-ifib-cfg:id1 = ' + str(self.id1) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.id1 is not None:
                                    return True

                                if self.rate is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:nps'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.np is not None:
                                for child_ref in self.np:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.id1 is None:
                            raise YPYDataValidationError('Key property id1 is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local-table[Cisco-IOS-XR-lpts-pre-ifib-cfg:id1 = ' + str(self.id1) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.id1 is not None:
                            return True

                        if self.nps is not None and self.nps._has_data():
                            return True

                        if self.nps is not None and self.nps.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local-tables'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ipolicer_local_table is not None:
                        for child_ref in self.ipolicer_local_table:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ipolicer_local is not None and self.ipolicer_local._has_data():
                    return True

                if self.ipolicer_local is not None and self.ipolicer_local.is_presence():
                    return True

                if self.ipolicer_local_tables is not None and self.ipolicer_local_tables._has_data():
                    return True

                if self.ipolicer_local_tables is not None and self.ipolicer_local_tables.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal']['meta_info']

        @property
        def _common_path(self):
            if self.node_name is None:
                raise YPYDataValidationError('Key property node_name is None')

            return '/Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes/Cisco-IOS-XR-config-mda-cfg:preconfigured-node[Cisco-IOS-XR-config-mda-cfg:node-name = ' + str(self.node_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.node_name is not None:
                return True

            if self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold._has_data():
                return True

            if self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.is_presence():
                return True

            if self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_wd_cfg_watchdog_node_threshold._has_data():
                return True

            if self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.is_presence():
                return True

            if self.lpts_local is not None and self.lpts_local._has_data():
                return True

            if self.lpts_local is not None and self.lpts_local.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.preconfigured_node is not None:
            for child_ref in self.preconfigured_node:
                if child_ref._has_data():
                    return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.config._meta import _Cisco_IOS_XR_config_mda_cfg as meta
        return meta._meta_table['PreconfiguredNodes']['meta_info']

