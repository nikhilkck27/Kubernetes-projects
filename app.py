from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory database simulation
items = []

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        abort(400)
    item = {
        'id': len(items) + 1,
        'name': request.json['name']
    }
    items.append(item)
    return jsonify(item), 201

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

# Get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    return jsonify(item)

# Update an item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    if not request.json or not 'name' in request.json:
        abort(400)
    item['name'] = request.json['name']
    return jsonify(item)

# Delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    items.remove(item)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
