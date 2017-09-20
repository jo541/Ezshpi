from flask import Blueprint
app = Blueprint('routes', __name__)

from .index import *
from photo import *