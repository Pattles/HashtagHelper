from flask import Flask, request, render_template, jsonify, redirect
import json
import random
import requests
import sqlite3
from flashtext import KeywordProcessor
import discord

google_maps_api_key = 'AIzaSyAKbCR95V5B9dvUtfbkc-_uAYqoGJvWj9o'
