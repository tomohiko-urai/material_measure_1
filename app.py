# coding: utf-8
import cv2
import numpy as np
import streamlit as st



# グローバル変数
point1 = None
point2 = None
scale = 0.0
scale_set = False
measuring = False
display_result = False  # 測定結果を表示するかどうか


# 2点間のユークリッド距離を計算
def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# マウスイベントのコールバック関数
def on_mouse(event, x, y, flags, param):
    global point1, point2, scale, scale_set, measuring

    # 左クリック時の処理
    if event == cv2.EVENT_LBUTTONDOWN:
        if point1 is None:
            point1 = (x, y)
            st.write(f"Point 1 set at: {point1}")
            #print(f"Point 1 set at: {point1}")
        elif point2 is None:
            point2 = (x, y)
            st.write(f"Point 2 set at: {point2}")
            #print(f"Point 2 set at: {point2}")
            
            st.write("standard_mode-not real_legth_start")
            #st.write("standard_mode-not real_legth_start",real_length)
           # measuring = True
            # 基準物のスケールを入力
            #while not real_length: 
            #real_length = st.text_input("Enter the real length between the two points in cm: ",)
            st.write("standard_mode-not scale_set_start")
              #st.write("standard_mode-not scale_set_start",real_length)
            while not scale_set:
              if not scale_set:
                #real_length = st.text_input("Enter the real length between the two points in cm: ",)
                st.write("standard_mode-1")
                real_length = st.text_input("Enter the real length between the two points in cm: ",3)
                #while True:
                  
                st.write("standard_mode-1")
                if  real_length:   
                       real_length = float(real_length)  
                #real_length = float(input("Enter the real length between the two points in cm: "))
                       pixel_distance = calculate_distance(point1, point2)
                       scale = real_length / pixel_distance
                       scale_set = True
                       st.write(f"Scale set to: {scale} cm/px")
                #print(f"Scale set to: {scale} cm/px")
           
                       st.write("standard_mode")
                      # break 
                        #print("standard_mode")
               
                    #st.write("whilereal_length_mode")
              st.write("while_not_sacle_set_mode")
               #measuring = True
              #break  
               #else:
                # 測定モードに移行
            measuring = True
            display_result = True  # 測定結果を表示するかどうか
 
               # print("measure_mode else ")
# カメラを起動
cap = cv2.VideoCapture(12)
#cap = cv2.VideoCapture(2)
#cap = cv2.VideoCapture(1)
#cap = cv2.VideoCapture(0)
cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", on_mouse)

while True:
    ret, frame = cap.read()
    if not ret:
        st.write("Failed to capture image")
        #print("Failed to capture image")
        break

    #cv2.setMouseCallback("Camera1", on_mouse)
    # マウスで選択された点を描画
      
    #print("point1")
    if point1 is not None:
        cv2.circle(frame, point1, 5, (0, 0, 255), -1)  # Point 1
    
    #print("point2")
    if point2 is not None:
        cv2.circle(frame, point2, 5, (0, 0, 255), -1)  # Point 2
        cv2.line(frame, point1, point2, (0, 255, 0), 2)  # Line between points

    # 測定モードで別の距離を測定
   


 
    #print("point1=",point1)
    #print("point2=",point2)
    #print("measuring=",measuring)
    #print("scale_set=",scale_set)
    if measuring and scale_set and point1 is not None and point2 is not None:
        pixel_distance = calculate_distance(point1, point2)
        real_distance = pixel_distance * scale
        cv2.putText(frame, f"{real_distance:.2f} cm", (point2[0], point2[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        measuring = False  # 測定を1回に制限してリセット
        st.write("real_distance= ",real_distance)
        #print("real_distance= ",real_distance)
        #print("real_distance= ",real_distance)
        #print("sotei mode-1 ")
        st.write("sotei mode-1 ")
    #cv2.imshow("Camera1", frame)
    cv2.imshow("Camera", frame)
    #image_loc = st.empty()
    #image_loc.image(frame) 
    # 'q'キーで終了
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    # 測定後、次の測定に備えてリセット
    if not measuring and scale_set and point1 is not None and point2 is not None: 
    #if not measuring and scale_set:
    #if measuring:
        point1 = None
        point2 = None
        display_result = False  # 測定結果の表示をオフにする 
        #measuring = False
       # print("measuring -false ")
    # 次のクリックがあるまで測定結果を表示する
  #  if measuring:
  #      measuring = False  

    #print("measuring-finish =",measuring)
    #st.write("measuring-finish =",measuring)

# カメラリソースを解放してウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()

