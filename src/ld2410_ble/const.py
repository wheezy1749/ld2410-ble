CHARACTERISTIC_NOTIFY = "0000fff1-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_WRITE = "0000fff2-0000-1000-8000-00805f9b34fb"

CMD_PREAMBLE                =                b"\xfd\xfc\xfb\xfa"
CMD_POSTAMBLE               =                b"\x04\x03\x02\x01"
CMD_BT_PASS_PRE             = CMD_PREAMBLE + b"\x08\x00\xa8\x00"
CMD_BT_PASS_DEFAULT         =                b"HiLink"
CMD_BT_PASS_POST            = CMD_POSTAMBLE
CMD_ENABLE_CONFIG           = CMD_PREAMBLE + b"\x04\x00\xff\x00\x01\x00" + CMD_POSTAMBLE
CMD_ENABLE_ENGINEERING_MODE =                b"\x02\x00b\x00" + CMD_POSTAMBLE
CMD_DISABLE_CONFIG          = CMD_PREAMBLE + b"\x02\x00\xfe" + CMD_POSTAMBLE

MOVING_TARGET = 1
STATIC_TARGET = 2

MAX_GATES = 9
MAX_SENSE_VAL = 100
MIN_SENSE_VAL = 0

frame_start = b"\xf4\xf3\xf2\xf1"
frame_length = b"(?P<length>..)"
frame_engineering_mode = b"(?P<engineering>\x01|\x02)"
frame_head = b"\xaa"
frame_target_state = b"(?P<target_state>\x00|\x01|\x02|\x03)"
frame_moving_target_distance = b"(?P<moving_target_distance>..)"
frame_moving_target_energy = b"(?P<moving_target_energy>.)"
frame_static_target_distance = b"(?P<static_target_distance>..)"
frame_static_target_energy = b"(?P<static_target_energy>.)"
frame_detection_distance = b"(?P<detection_distance>..)"
frame_engineering_data = b"(?P<engineering_data>.+?)?"
frame_tail = b"\x55"
frame_check = b"\x00"
frame_end = b"\xf8\xf7\xf6\xf5"

frame_maximum_motion_gates = b"(?P<maximum_motion_gates>.)"
frame_maximum_static_gates = b"(?P<maximum_static_gates>.)"
frame_motion_energy_gates = b"(?P<motion_energy_gates>.{9})"
frame_static_energy_gates = b"(?P<static_energy_gates>.{9})"
frame_additional_information = b"(?P<additional_information>.*)"

frame_regex = (
    frame_start
    + frame_length
    + frame_engineering_mode
    + frame_head
    + frame_target_state
    + frame_moving_target_distance
    + frame_moving_target_energy
    + frame_static_target_distance
    + frame_static_target_energy
    + frame_detection_distance
    + frame_engineering_data
    + frame_tail
    + frame_check
    + frame_end
)

engineering_frame_regex = (
    frame_maximum_motion_gates
    + frame_maximum_static_gates
    + frame_motion_energy_gates
    + frame_static_energy_gates
    + frame_additional_information
)
