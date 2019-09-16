#!/usr/bin/env python
# -*- coding: utf-8 -*-




class RobotData(object):
    
    def __init__(self, robot_name, robotID, hPeriod, neig_timeout, position):
        self.robot_id = robotID
        self.hello_period = h_Period
        self.neighbor_timeout = neig_timeout
        self.onehopList = list()
        self.robot_degree = 0
        self.rngList = list()
        self.rng_degree = 0
        self.robot_name = robot_name
        self.hello_tx = 0
        self.hello_rx = 0
        self._position = position

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, pos):
        self._position = pos
        
    def __repr__(self):
        return "RobotData({}, {}, {}, {}, {}, {}, {}, {}, {})" .format(repr(self.robotID), repr(self.robot_name), repr(self.onehopList), repr(self.robot_degree), repr(self.rngList), 
                                                                       repr(self.rng_degree), repr(self.hello_tx), repr(self.hello_rx), repr(self.position))
                                                                            
    def __str__(self):
        return "({}, {}, {}, {}, {}, {}, {}, {}, {})" .format(self.robotID, self.robot_name, str(self.onehopList), self.robot_degree, str(self.rngList), self.rng_degree, self.hello_tx, 
                                                              self.hello_rx, str(self.position))
