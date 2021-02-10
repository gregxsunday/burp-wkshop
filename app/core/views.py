from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify
from app.core.repository import *

from base64 import b64encode 
from urllib.parse import quote_plus

mod = Blueprint('core', __name__)

flags = {
  'history': r'msfi{123}',
  'intercept': r'msfi{456}',
  'repeater': r'msfi{789}',
  'intruder': r'msfi{0ab}',
  'decoder': r'msfi{cde}'
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

@mod.route('/intercept', methods=['GET','POST'])
def intercept():
  if request.method == 'POST':
    if request.form['i_want_the_flag'] == 'yes':
      return f'<html>{flags["intercept"]}</html>'
    else:
      return f'<html>no flag for you</html>'
  else:
    return (render_template('core/intercept.html', nav='intercept'))

@mod.route('/repeater')
def repeater():
  return (render_template('core/repeater.html', nav='repeater'))

@mod.route('/repeater.json', methods=['GET', 'POST', 'PUT'])
def repeater_json():
  if request.method == 'PUT':
    if request.is_json:
      req = request.get_json()
      try:
        key = req['key']
        # TODO key z enva
        if key == 5:
          return jsonify({'flag': flags['repeater']})
        else:
          return jsonify({'error':'this is not the correct key my friend'})
      except KeyError:
        return jsonify({'error':'I want the key in the JSON my friend'}), 400
    else:
      return jsonify({'error':'I want JSON my friend'}), 400
  else:
    return jsonify({'error':'Bad method my friend'}), 405

@mod.route('/intruder')
def intruder():
  return (render_template('core/intruder.html', nav='intruder'))

@mod.route('/intruder.json', methods=['GET', 'POST', 'PUT'])
def intruder_json():
  if request.method == 'PUT':
    if request.is_json:
      req = request.get_json()
      try:
        key = req['key']
        # TODO key z enva
        if key == 2:
          return jsonify({'flag': flags['intruder']})
        else:
          return jsonify({'error':'this is not the correct key my friend'})
      except KeyError:
        return jsonify({'error':'I want the key in the JSON my friend'}), 400
    else:
      return jsonify({'error':'I want JSON my friend'}), 400
  else:
    return jsonify({'error':'Bad method my friend'}), 405

def encode_flag(flag):
  flag = quote_plus(flag)
  flag = b64encode(flag.encode('utf8'))
  flag = str(flag)[2:-1]
  flag = ''.join(list(map(lambda x: hex(ord(x))[2:], flag)))
  flag = b64encode(flag.encode('utf8'))
  flag = str(flag)[2:-1]
  return flag


@mod.route('/decoder')
def decoder():
  flag = flags['decoder']
  flag = encode_flag(flag)
  return (render_template('core/decoder.html', nav='decoder', flag=flag))