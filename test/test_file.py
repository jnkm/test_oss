from unittest import TestCase

import hello_world
import somewhattested

class MyTestCase(TestCase):
  def test_pass(self):
    return

  def test_qwerty(self):
    assert somewhattested.qwerty() == 6
