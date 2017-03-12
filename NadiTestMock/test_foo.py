from unittest import TestCase
from old import Old
from foo import Foo
#from mock import patch
import mock

class TestFoo(TestCase):
    def test_method_1(self):
        old1 = Old(5)
        foo1 = Foo(old1)
        x = foo1.method_1()
        TestCase.assertEquals(self,x, 5)

    def mock_method_1(self):
        return 10

    @mock.patch('foo.Foo.method_1', side_effect=mock_method_1)
    def test_method_1(self,mock_method_1):
        old1 = Old(5)
        assert Foo(old1).method_1(self) == 10


    def mock_returnX(self):
        return 20

    @mock.patch('old.Old.returnX')
    def test_method_1(self,mock_returnX):
        mock_returnX.return_value = 20
        old1 = Old(5)
        TestCase.assertEquals(self, Foo(old1).method_1(), 20)