from dataclasses import dataclass
from typing import Any
from flask import Flask, render_template, request, jsonify
import yaml

from scripts.classes import AppConfig, Board, VisualConfig, GameConfig

app = Flask(__name__)

# Global state: app config and board persisted in memory while the server runs
appConfig_global: AppConfig | None = None
board_global: Board | None = None

def setup() -> AppConfig:
    appConfig: AppConfig = None

    with open('settings.yml', 'r') as file:
        raw_config = yaml.safe_load(file)

        visual = VisualConfig(
            title = raw_config['settings']['visual']['title'],
            font = raw_config['settings']['visual']['font'],
            textSize = raw_config['settings']['visual']['textSize'],
            width = raw_config['settings']['visual']['width'],
            height = raw_config['settings']['visual']['height'],
            menuWidth = raw_config['settings']['visual']['menuWidth'],
            icon = raw_config['settings']['visual']['icon'],
            cellSize = int(raw_config['settings']['visual']['width'] / raw_config['settings']['game']['xGrid']),
            size = (raw_config['settings']['visual']['width'] + raw_config['settings']['visual']['menuWidth'], raw_config['settings']['visual']['height'])
        )

        game = GameConfig(
            whiteStarts = raw_config['settings']['game']['whiteStarts'],
            blackAndWhiteColor = raw_config['settings']['game']['blackAndWhiteColor'],
            xGrid = raw_config['settings']['game']['xGrid'],
            yGrid = raw_config['settings']['game']['yGrid'],
            AI = raw_config['settings']['game']['AI']
        )

        appConfig = AppConfig(visual, game)

    if appConfig is None:
        raise ValueError("Failed to load configuration.")

    return appConfig


def ensure_initialized():
    """Initialize global app config and board once."""
    global appConfig_global, board_global
    if appConfig_global is None:
        appConfig_global = setup()
    if board_global is None:
        board_global = Board(appConfig_global)


@app.route('/', methods=["GET"])
def main():
    ensure_initialized()
    return render_template('index.html', appConfig=appConfig_global, board=board_global)


@app.route('/move', methods=['POST'])
def move_piece():
    """Receive a JSON payload with 'from' and 'to' coordinates and update the board."""
    ensure_initialized()
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'ok': False, 'error': 'Invalid JSON'}), 400

    try:
        src = data.get('from')
        dst = data.get('to')
        sx, sy = int(src[0]), int(src[1])
        dx, dy = int(dst[0]), int(dst[1])
    except Exception as e:
        return jsonify({'ok': False, 'error': 'Invalid payload format'}), 400

    # bounds check
    if not (0 <= sx < appConfig_global.game.xGrid and 0 <= sy < appConfig_global.game.yGrid and 0 <= dx < appConfig_global.game.xGrid and 0 <= dy < appConfig_global.game.yGrid):
        return jsonify({'ok': False, 'error': 'Out of bounds'}), 400

    piece = board_global.pieces[sx][sy]
    if piece is None:
        return jsonify({'ok': False, 'error': 'No piece at source'}), 400

    # perform move (simple overwrite / capture behavior)
    piece.position = [dx, dy]
    board_global.pieces[dx][dy] = piece
    board_global.pieces[sx][sy] = None

    return jsonify({'ok': True})


if __name__ == '__main__':
    ensure_initialized()
    app.run(host="0.0.0.0", debug=True)