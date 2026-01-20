import cv2

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)

    players = {}
    player_id = 1
    frame_count = 0

    while cap.isOpened() and frame_count < 300:
        ret, frame = cap.read()
        if not ret:
            break

        if player_id not in players:
            players[player_id] = {
                "points": 0,
                "rebounds": 0,
                "assists": 0
            }

        players[player_id]["points"] += 2
        frame_count += 30
        player_id += 1

    cap.release()
    return players
