# import sys
# from celery import Celery
#
# sys.path.append('imr')
# from imr import imr
#
# cApp = Celery('tasks', broker='redis://redis')
#
# @cApp.task
# def gen():
#   imr()
#   return True
