from unittest import TestCase

import hello_world
import tested

class MyTestCase(TestCase):
  def test_pass(self):
    return

  def test_qwerty(self):
    assert tested.qwerty() == 6
