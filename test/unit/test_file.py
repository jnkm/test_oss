from unittest import TestCase

import hello_world
import untested

class MyTestCase(TestCase):
  def test_pass(self):
    return

  def test_qwerty(self):
    assert untested.qwerty() == 6

  def test_hi_name(self):
    assert hello_world.say_hi('jim') == 'hi jim'
