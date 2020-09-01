# smoking_calling
- image_processor_boader.py
  - 包含的一些图像边界的填充方法  
  
- train_image_processor.py
  - 对训练图像进行处理
    - 对训练图像进行边界填充
    - 对训练图像进行缩放
    - 对训练图像转数据转换成为浮点型
    - 对训练图像进行分类进行编码
      - {'calling': 0, 'normal': 1, 'smoking': 2}

