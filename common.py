from flask import Flask, request, render_template, jsonify
import json
import requests
import sqlite3
from flashtext import KeywordProcessor

google_maps_api_key = 'AIzaSyA3BVGehNIwyoFXC_mYgrOnntTbtMuzp20'
