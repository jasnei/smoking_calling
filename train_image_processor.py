import cv2
def train_image_processor(path):
    resize_rows = 224
    resize_cols = 224

    folders = os.listdir(path)
    label_dict = {'calling': 0, 'normal': 1, 'smoking': 2}
    train_image = []
    train_label = []

    for folder in folders:
        folder_path = os.path.join(path, folder)
        # 判断是否文件夹
        if os.path.isdir(folder_path):
            # 返回所有的文件名
            files = os.listdir(folder_path)
            # 得到文件名下的标签
            folder_lable = label_dict[folder.split('_')[0]]        
            print(folder_lable,len(files))
            # 得到所有的图像数据
            for file in files:
                image_path = os.path.join(folder_path, file)
                img = cv2.imread(image_path)

                # 保持纵横比例变成正方形
                if img.shape[1] > img.shape[0]:
                    top = 0
                    left = 0
                    bottom = img.shape[1] - img.shape[0]
                    right = 0
                elif img.shape[0] > img.shape[1]:
                    top = 0
                    left = 0
                    bottom = 0
                    right = img.shape[0] - img.shape[1]  

                img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_DEFAULT)           
                img_resize = cv2.resize(img_with_border, (resize_rows, resize_cols), cv2.INTER_AREA)
                img_arry = np.array(img_resize).astype(np.float32)
                train_image.append(img_arry)
                train_label.append(folder_lable)
    return train_image, train_label