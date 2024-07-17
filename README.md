# globalLocalDL

## Overview
The globalLocalDL framework integrates the global-local approach with deep learning to bypass the fidelity and performance barrier that exists on the thermal process simulation side. The Transformer model converts the layerwise data to scanwise, enabling part-scale grain structure modeling.

1. **Data Preprocessing:** Separate coordinates and features, normalize the data.
2. **Model Construction:** Build the Transformer model architecture.
3. **Model Training:** Train and validate the model using the provided dataloader and GPU capabilities.

## Features
- **GPU Implementation:** Uses CUDA to transfer model computations and data processing to the GPU, significantly speeding up the training process. 
Mixed precision training is employed to reduce memory usage by combining 16-bit and 32-bit floating-point computations.
- **Sliding Window Approach:** Segments data into smaller, overlapping windows, allowing for effective handling of varied input dimensions, enhanced temporal dependency capture, and efficient data loading and memory management.
- **Memory Handling:** Balances training efficiency and memory usage through careful parameter selection (batch size, window size), implements gradient accumulation to allow for larger effective batch sizes, and optimizes the number of worker threads for efficient data loading.
