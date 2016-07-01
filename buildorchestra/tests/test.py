from unittest import TestCase

from buildorchestra.build import Builder


class Test(TestCase):
  def test_simple_dependencies(self):
    builder = Builder()
    builder.add_build_step("a", [], lambda **options: print("a"))
    builder.add_build_step("b", ["a"], lambda **options: print("b"))
    builder.add_build_step("c", ["b"], lambda **options: print("c"))
    builder.add_build_step("d", ["a"], lambda **options: print("d"))
    builder.add_build_step("e", [], lambda **options: print("e"))
    builder.build("c")
