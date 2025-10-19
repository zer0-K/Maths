#############################
#                           #
#       Test utilities      #
#                           #
#############################

import sys
import traceback
from typing import Dict
from collections.abc import Callable

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger


class CST:
    
    success: str = "good"
    fail: str = "fail"


class TestContainer:
    
    def __init__(self, inputs: list[any] = None, expected_outputs: list[any] = None):

        if inputs is None:
            inputs = []
        if expected_outputs is None:
            expected_outputs = []

        # check integrity
        if len(inputs) != len(expected_outputs):
            Logger.error("Inputs and expected outputs don't have the same length...", "[TestContainer][__init__]")
        
        self.inputs: list[any] = inputs
        self.expected_outputs: list[any] = expected_outputs

    def add(self, new_input: any, new_expected_output: any):
        self.inputs.append(new_input)
        self.expected_outputs.append(new_expected_output)


class UtilsTest:
    """Test utilities
    Set stop_test_on_fail to True if you want the program to stop if a test fails
    """
    
    stop_test_on_fail: bool = False

    @staticmethod
    def check(func_to_test: Callable, test_container: TestContainer, log_prefix: str, 
              is_expected_to_fail: bool = False) -> str:
        """some tests tests that some cases fail : in that case set is_expected_to_fail to true"""
        global_success: str = CST.success 

        for x, y_ in zip(test_container.inputs, test_container.expected_outputs):
            # preprocess
            success: str = CST.success

            # process
            if True:
                try:
                    y = func_to_test(x)
                    if y != y_ and not is_expected_to_fail:
                        err_msg: str = f"Failed on inputs : {x}. Got {y} instead of {y_}."
                        success = CST.fail
                    elif y == y_ and is_expected_to_fail:
                        err_msg: str = f"Failed on inputs : {x}. Test was expected to fail " + \
                            f"but results matched (got {y}, expected: {y_})."
                        success = CST.fail
                        
                except Exception as e:
                    y = None
                    if not is_expected_to_fail:
                        err_msg: str = f"Failed on inputs : {x}.\n{traceback.format_exc()}"
                        success = CST.fail

            # postprocess
            if True:
                if success == CST.fail:
                    global_success = CST.fail
                    Logger.error(err_msg, log_prefix)

                    if UtilsTest.stop_test_on_fail:
                        raise Exception(f"Stopping tests. {log_prefix} {err_msg}")
        
        return global_success
