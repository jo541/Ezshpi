from flask import Blueprint
app = Blueprint('routes', __name__)

from easy_photo_share.app import models
from .index import *
from photo import *