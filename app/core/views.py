from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify
from app.core.repository import *

mod = Blueprint('core', __name__)

flags = {
  'history': r'msfi{123}'
}

@mod.route('/')
def index():
  return (render_template('core/index.html', nav='setup'))

@mod.route('/history2')
def history2():
  return f'<html>{flags["history"]}</html>'

@mod.route('/history')
def history():
  return (render_template('core/history.html', nav='history'))