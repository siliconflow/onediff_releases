## Install OneDiff Enterprise

[![Daily Build](https://github.com/siliconflow/onediff_releases/actions/workflows/pack_wheel.yml/badge.svg)](https://github.com/siliconflow/onediff_releases/actions/workflows/pack_wheel.yml)

### For NA/EU users

**CUDA 11.8**

```bash
python3 -m pip install --pre oneflow -f https://github.com/siliconflow/oneflow_releases/releases/expanded_assets/enterprise_cu118 && \
python3 -m pip install --pre onediff-quant -f https://github.com/siliconflow/onediff_releases/releases/expanded_assets/enterprise && \
python3 -m pip install git+https://github.com/siliconflow/onediff.git@main#egg=onediff
```

**CUDA 12.1**

```bash
python3 -m pip install --pre oneflow -f https://github.com/siliconflow/oneflow_releases/releases/expanded_assets/enterprise_cu121 && \
python3 -m pip install --pre onediff-quant -f https://github.com/siliconflow/onediff_releases/releases/expanded_assets/enterprise && \
python3 -m pip install git+https://github.com/siliconflow/onediff.git@main#egg=onediff
```

**CUDA 12.2**

```bash
python3 -m pip install --pre oneflow -f https://github.com/siliconflow/oneflow_releases/releases/expanded_assets/enterprise_cu122 && \
python3 -m pip install --pre onediff-quant -f https://github.com/siliconflow/onediff_releases/releases/expanded_assets/enterprise && \
python3 -m pip install git+https://github.com/siliconflow/onediff.git@main#egg=onediff
```

### For CN users

**CUDA 11.8**

```bash
python3 -m pip install --pre oneflow -f https://oneflow-pro.oss-cn-beijing.aliyuncs.com/branch/main/cu118/ && \
python3 -m pip install --pre onediff-quant -f https://oneflow-pro.oss-cn-beijing.aliyuncs.com/onediff-quant/ && \
python3 -m pip install git+https://github.com/siliconflow/onediff.git@main#egg=onediff
```

**CUDA 12.1**

```bash
python3 -m pip install --pre oneflow -f https://oneflow-pro.oss-cn-beijing.aliyuncs.com/branch/main/cu121/ && \
python3 -m pip install --pre onediff-quant -f https://oneflow-pro.oss-cn-beijing.aliyuncs.com/onediff-quant/ && \
python3 -m pip install git+https://github.com/siliconflow/onediff.git@main#egg=onediff
```

**CUDA 12.2**

```bash
python3 -m pip install --pre oneflow -f https://oneflow-pro.oss-cn-beijing.aliyuncs.com/branch/main/cu122/ && \
python3 -m pip install --pre onediff-quant -f https://oneflow-pro.oss-cn-beijing.aliyuncs.com/onediff-quant/ && \
python3 -m pip install git+https://github.com/siliconflow/onediff.git@main#egg=onediff
```
