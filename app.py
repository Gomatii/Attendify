from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
import cv2
import os

app = Flask(__name__)


# Load the pre-trained model
#model = load_model('face_detection_model.h5')

# Directory to save captured images
BASE_SAVE_DIR = 'images'
if not os.path.exists(BASE_SAVE_DIR):
    os.makedirs(BASE_SAVE_DIR)

# Initialize webcam
camera = cv2.VideoCapture(0)

# Dictionary to keep track of image counts for each person
image_counts = {}

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    name = request.form['name']
    id_ = request.form['id']
    if not name or not id_:
        return "Name and ID are required!", 400

    # Create directory for the person if it doesn't exist
    person_dir = os.path.join(BASE_SAVE_DIR, f"{name}_{id_}")
    if not os.path.exists(person_dir):
        os.makedirs(person_dir)

    # Initialize or update the image count for the person
    person_key = f"{name}_{id_}"
    if person_key not in image_counts:
        image_counts[person_key] = 0

    # Read frame from the camera
    success, frame = camera.read()
    if success:
        # Save the captured image
        img_count = image_counts[person_key]
        if img_count < 10:
            img_name = f"{name}_{id_}_{img_count + 1}.jpg"
            img_path = os.path.join(person_dir, img_name)
            cv2.imwrite(img_path, frame)
            image_counts[person_key] += 1
            return jsonify({"message": f"Image {img_count + 1} saved at {img_path}"})
        else:
            return jsonify({"message": f"Already captured 10 images for {name}_{id_}"}), 400
    else:
        return jsonify({"message": "Failed to capture image"}), 500

if __name__ == '__main__':
    app.run(debug=True)
