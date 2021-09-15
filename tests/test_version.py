import os
class TestBake(object):

    def test_default(self, cookies):

        result = cookies.bake()

        assert result.exit_code == 0
        assert result.exception is None

        assert result.project_path.name == "xeus-mylang"
        assert result.project_path.is_dir()



        # remember the directory where tests should be run from
        cwd = os.getcwd()
        # change directories to the generated project directory 
        os.chdir(str(project.project))
        try:
            pass
        except sh.ErrorReturnCode as e:
            # print the error, so we know what went wrong
            print(e)
            # make sure the test fails
            pytest.fail(e)
        finally:
            # always change directories to the test directory
            os.chdir(cwd)