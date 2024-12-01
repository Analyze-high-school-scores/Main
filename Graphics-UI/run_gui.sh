#!/bin/bash

MAIN_FILE="main.py"
VENV_NAME="venv"

check_libraries() {
  if python3 -c "import pandas, numpy, matplotlib, tkinter" 2>/dev/null; then
    echo "Đã có đầy đủ thư viện, chạy trực tiếp ứng dụng..."
    python3 "$MAIN_FILE"
    exit 0
  fi
  return 1
}

check_os() {
  if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Đang chạy trên macOS"
    PYTHON="python3"
    PIP="pip3"
  else
    echo "Đang chạy trên Linux"
    PYTHON="python3"
    PIP="pip3"
  fi
}

setup_python() {
  if ! command -v $PYTHON &>/dev/null; then
    echo "Python3 chưa được cài đặt. Đang cài đặt..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
      brew install python3
    else
      sudo apt-get update
      sudo apt-get install python3 python3-pip python3-venv python3-tk
    fi
  fi
}

setup_venv() {
  echo "Đang tạo môi trường ảo..."
  $PYTHON -m venv $VENV_NAME
  source $VENV_NAME/bin/activate
}

install_requirements() {
  echo "Đang cài đặt các thư viện cần thiết..."
  $PIP install pandas numpy matplotlib tk requests
}

run_app() {
  echo "Đang khởi động ứng dụng..."
  if [ -f "$MAIN_FILE" ]; then
    $PYTHON "$MAIN_FILE"
  else
    echo "Không tìm thấy file $MAIN_FILE"
    exit 1
  fi
}

cleanup() {
  echo "Đang dọn dẹp..."
  deactivate
  echo "Đã tắt môi trường ảo"
}

main() {
  check_libraries || {
    echo "Thiếu thư viện, tiến hành cài đặt..."
    check_os
    setup_python

    if [ ! -d "$VENV_NAME" ]; then
      setup_venv
    else
      source $VENV_NAME/bin/activate
    fi

    install_requirements
    trap cleanup EXIT
    run_app
  }
}

main
