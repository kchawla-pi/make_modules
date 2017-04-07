import unittest
import os

from create_module import path
# from create_module import if __name__ == '__main__':


class CreateModuleTest(unittest.TestCase):
    def __init__(self):

        def create_test_data(self):

            create_module_path = os.getcwd()  # "C:/Users/kshit/Dropbox/libraries/kc/workspace/kc/tic_modules"
            tests_path_dirs = create_module_path.split(os.sep)
            tests_path_dirs.append('tests')
            tests_path_dirs.append('data')
            tests_data_path = os.sep.join(tests_path_dirs)
            tests_subtree_dirs = list()

            for ls_entry in os.scandir(tests_data_path):
                if ls_entry.name[:4] == 'tic_' and ls_entry.is_dir():
                    temp = tests_path_dirs + [ls_entry.name, ls_entry.name[4:]]
                    tests_subtree_dirs.append(temp)

            test_dir_start_idx = len(create_module_path.split(os.sep))

            tests_subtrees = [os.sep.join(dirs[test_dir_start_idx:]) for dirs in tests_subtree_dirs]

        create_test_data(self)



    def test_path(self):
        for case in range(0, len(self.tests_subtrees)):
            path_fn_returns = path(self.tests_subtrees[case])
            expected_value = os.sep.join(self.tests_subtree_dirs[case])
            self.assertEqual(path_fn_returns, expected_value)


unittest.main()