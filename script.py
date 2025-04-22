from graphviz import Digraph

dot = Digraph(format='png')
dot.attr(rankdir='TB', fontsize='10')

# Node styles
dot.attr('node', shape='box', style='filled', color='#f6f6ff', fontname='Helvetica')
diamond_attr = {'shape': 'diamond', 'style': 'filled', 'color': '#f6f6ff', 'fontname': 'Helvetica'}

# Define nodes
dot.node('start', 'Start')
dot.node('init', 'Initialize Serial and GPS')
dot.node('wifi', 'Connect to WiFi')
dot.node('loop', 'Start Loop')
dot.node('read', 'Read GPS Data')
dot.node('process', 'Process GPS Data')
dot.node('validity', 'Check GPS Validity')

dot.node('time', 'Time to Upload?', **diamond_attr)
dot.node('gps', 'GPS Valid?', **diamond_attr)
dot.node('interval', 'Check Upload Interval')
dot.node('skip', 'Skip Upload')

dot.node('upload', 'Upload Data')
dot.node('sendOffline', 'Send Offline Data If Any')
dot.node('sendSuccess1', 'Send Success?', **diamond_attr)
dot.node('clear', 'Clear Offline Data')
dot.node('sendLatest', 'Send Latest GPS Data')
dot.node('sendSuccess2', 'Send Success?', **diamond_attr)
dot.node('uploadSuccess', 'Upload Successful')
dot.node('storeOffline', 'Store Data Offline')

# Edges
dot.edge('start', 'init')
dot.edge('init', 'wifi')
dot.edge('wifi', 'loop')
dot.edge('loop', 'read')
dot.edge('read', 'process')
dot.edge('process', 'validity')

dot.edge('validity', 'time')

dot.edge('time', 'upload', label='Yes')
dot.edge('time', 'gps', label='No')

dot.edge('gps', 'interval', label='Yes')
dot.edge('gps', 'skip', label='No')
dot.edge('interval', 'loop')
dot.edge('skip', 'loop')

dot.edge('upload', 'sendOffline')
dot.edge('sendOffline', 'sendSuccess1')
dot.edge('sendSuccess1', 'clear', label='Yes')
dot.edge('clear', 'sendLatest')
dot.edge('sendLatest', 'sendSuccess2')
dot.edge('sendSuccess2', 'uploadSuccess', label='Yes')
dot.edge('sendSuccess2', 'storeOffline', label='No')
dot.edge('sendSuccess1', 'storeOffline', label='No')

# Render and save
dot.render('gps_upload_flowchart', cleanup=False)
print("Flowchart rendered to 'gps_upload_flowchart.png'")
