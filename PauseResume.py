import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#from qt import QTimer
import time

class QTimerWithPause (QTimer):
  def __init__ (self, parent = None, name = ""):
      QTimer.__init__ (self, parent, name)

      self.startTime = 0
      self.interval    = 0

  def startTimer (self, interval):
      self.interval    = interval
      self.startTime = time.time ()

      QTimer.start (self, interval, True) # one-shot

  def pause (self):
      if self.isActive ():
          self.stop ()

          elapsedTime    = self.startTime - time.time ()
	        self.startTime -= elapsedTime

          # time() returns float secs, interval is int msec
          self.interval -= int (elapsedTime*1000))

  def resume (self):
      if not self.isActive ():
          self.start (self.interval)