# validated: 2017-11-12 TW 21585f70a88e edu/wpi/first/wpilibj/XboxController.java
# ----------------------------------------------------------------------------
# Copyright (c) FIRST 2016-2017. All Rights Reserved.
# Open Source Software - may be modified and shared by FRC teams. The code
# must be accompanied by the FIRST BSD license file in the root directory of
# the project.
# ----------------------------------------------------------------------------
import hal
from .driverstation import DriverStation
from .interfaces.generichid import GenericHID


class XboxController(GenericHID):
    """
        Handle input from Xbox 360 or Xbox One controllers connected to the Driver Station.

        This class handles Xbox input that comes from the Driver Station. Each time a value is
        requested the most recent value is returned. There is a single class instance for each controller
        and the mapping of ports to hardware buttons depends on the code in the Driver Station.
     """

    class Button:
        kBumperLeft = 5
        kBumperRight = 6
        kStickLeft = 9
        kStickRight = 10
        kA = 1
        kB = 2
        kX = 3
        kY = 4
        kBack = 7
        kStart = 8

    def __init__(self, port):
        """Construct an instance of an XBoxController. The XBoxController index is the USB port on the Driver Station.

        :param port: The port on the Driver Station that the joystick is plugged into
        """

        super().__init__(port)
        self.ds = DriverStation.getInstance()

        self.outputs = 0
        self.leftRumble = 0
        self.rightRumble = 0

        hal.report(hal.UsageReporting.kResourceType_Joystick, port)

    def getX(self, hand):
        """Get the X axis value of the controller.

        :param hand: Side of controller whose value should be returned
        :return: The X axis value of the controller
        :rtype: float
        """
        if hand == GenericHID.Hand.kLeft:
            return self.getRawAxis(0)
        else:
            return self.getRawAxis(4)

    def getY(self, hand):
        """Get the Y axis value of the controller.

        :param hand: Side of controller whose value should be returned
        :return: The Y axis value of the controller
        :rtype: float
        """
        if hand == GenericHID.Hand.kLeft:
            return self.getRawAxis(1)
        else:
            return self.getRawAxis(5)

    def getTriggerAxis(self, hand):
        """Get the trigger axis value of the controller.

        :param hand: Side of controller whose value should be returned
        :return: The trigger axis value of the controller
        :rtype: float
        """
        if hand == GenericHID.Hand.kLeft:
            return self.getRawAxis(2)
        else:
            return self.getRawAxis(3)

    def getBumper(self, hand):
        """Read the values of the bumper button on the controller.

        :param hand: Side of controller whose value should be returned.
        :return: The state of the button
        :rtype: boolean
        """
        if hand == GenericHID.Hand.kLeft:
            return self.getRawButton(self.Button.kBumperLeft)
        else:
            return self.getRawButton(self.Button.kBumperRight)

    def getBumperPressed(self, hand):
        """Whether the bumper was pressed since the last check.

        :param hand: Side of controller whose value should be returned.
        :returns: Whether the button was pressed since the last check.
        """
        if hand == GenericHID.Hand.kLeft:
            return self.getRawButtonPressed(self.Button.kBumperLeft)
        else:
            return self.getRawButtonPressed(self.Button.kBumperRight)

    def getBumperReleased(self, hand):
        """Whether the bumper was released since the last check.

        :param hand: Side of controller whose value should be returned.
        :returns: Whether the button was released since the last check.
        """
        if hand == GenericHID.Hand.kLeft:
            return self.getRawButtonReleased(self.Button.kBumperLeft)
        else:
            return self.getRawButtonReleased(self.Button.kBumperRight)

    def getStickButton(self, hand):
        """Read the values of the stick button on the controller

        :param hand: Side of the controller whose value should be returned
        :return: The state of the button
        :rtype: boolean
        """
        if hand == GenericHID.Hand.kLeft:
            return self.getRawButton(9)
        else:
            return self.getRawButton(10)

    def getStickButtonPressed(self, hand):
        """Whether the stick button was pressed since the last check.

        :param hand: Side of controller whose value should be returned.
        :return: Whether the button was pressed since the last check.
        """
        if hand == GenericHID.Hand.kLeft:
            return self.getRawButtonPressed(self.Button.kStickLeft)
        else:
            return self.getRawButtonPressed(self.Button.kStickRight)

    def getStickButtonReleased(self, hand):
        """Whether the stick button was released since the last check.

        :param hand: Side of controller whose value should be returned.
        :return: Whether the button was released since the last check.
        """
        if hand == GenericHID.Hand.kLeft:
            return self.getRawButtonReleased(self.Button.kStickLeft)
        else:
            return self.getRawButtonReleased(self.Button.kStickRight)

    def getAButton(self):
        """Read the value of the A button on the controller

        :return: The state of the A button
        :rtype: boolean
        """
        return self.getRawButton(self.Button.kA)

    def getAButtonPressed(self):
        """Whether the A button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self.getRawButtonPressed(self.Button.kA)

    def getAButtonReleased(self):
        """Whether the A button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self.getRawButtonReleased(self.Button.kA)

    def getBButton(self):
        """Read the value of the B button on the controller

        :return: The state of the B button
        :rtype: boolean
        """
        return self.getRawButton(self.Button.kB)

    def getBButtonPressed(self):
        """Whether the B button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self.getRawButtonPressed(self.Button.kB)

    def getBButtonReleased(self):
        """Whether the B button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self.getRawButtonReleased(self.Button.kB)

    def getXButton(self):
        """Read the value of the X button on the controller

        :return: The state of the X button
        :rtype: boolean
        """
        return self.getRawButton(self.Button.kX)

    def getXButtonPressed(self):
        """Whether the X button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self.getRawButtonPressed(self.Button.kX)

    def getXButtonReleased(self):
        """Whether the X button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self.getRawButtonReleased(self.Button.kX)

    def getYButton(self):
        """Read the value of the Y button on the controller

        :return: The state of the Y button
        :rtype: boolean
        """
        return self.getRawButton(self.Button.kY)

    def getYButtonPressed(self):
        """Whether the Y button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self.getRawButtonPressed(self.Button.kY)

    def getYButtonReleased(self):
        """Whether the Y button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self.getRawButtonReleased(self.Button.kY)

    def getBackButton(self):
        """Read the value of the Back button on the controller

        :return: The state of the Back button
        :rtype: boolean
        """
        return self.getRawButton(self.Button.kBack)

    def getBackButtonPressed(self):
        """Whether the Back button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self.getRawButtonPressed(self.Button.kBack)

    def getBackButtonReleased(self):
        """Whether the Back button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self.getRawButtonReleased(self.Button.kBack)

    def getStartButton(self):
        """Read the value of the Start button on the controller

        :return: The state of the Start button
        :rtype: boolean
        """
        return self.getRawButton(self.Button.kStart)

    def getStartButtonPressed(self):
        """Whether the Start button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self.getRawButtonPressed(self.Button.kStart)

    def getStartButtonReleased(self):
        """Whether the Start button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self.getRawButtonReleased(self.Button.kStart)
