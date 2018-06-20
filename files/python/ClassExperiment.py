class TestClass(object):

    class_attribute = 3

    def a_method(self, one, two):
        instance_variable = one + two
        self.class_attribute = one + two
        return instance_variable


test1 = TestClass()
print('test1.class_attrivute =', test1.class_attribute)
TestClass.class_attribute = 5
print('test1.class_attribute =', test1.class_attribute)
test2 = TestClass()
print('test2.class_attribute =', test2.class_attribute)
print(test1.a_method(3, 4))
# print('TestClass.a_method =', TestClass.a_method(3, 4))
print(test1.class_attribute)
print(test2.class_attribute)
print(TestClass.class_attribute)