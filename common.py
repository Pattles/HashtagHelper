from flask import Flask, request, render_template, jsonify
import json
import requests
import sqlite3

google_maps_api_key = 'AIzaSyA3BVGehNIwyoFXC_mYgrOnntTbtMuzp20'

# MongoDB Credentials
"""
Database User Username: Cluster83411
Database User Password: UEZKb19Ebkx8
Your connection string: mongodb+srv://cluster83411.cuazoek.mongodb.net
"""