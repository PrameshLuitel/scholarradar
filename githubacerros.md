Skip to content
PrameshLuitel
scholarradar
Repository navigation
Code
Issues
Pull requests
Actions
Projects
Security and quality
Insights
Settings
Daily Supabase Scraper
 
Daily Supabase Scraper #9
All jobs
Run details
run-scraper
succeeded 2 minutes ago in 6m 17s

1s
2s
1s
/opt/hostedtoolcache/Python/3.11.15/x64/bin/pip cache dir
/home/runner/.cache/pip
pip cache is not found
27s
Run python -m pip install --upgrade pip
  
Requirement already satisfied: pip in /opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages (26.0.1)
Collecting mcp>=1.0.0 (from -r requirements.txt (line 1))
  Downloading mcp-1.27.0-py3-none-any.whl.metadata (8.2 kB)
Collecting supabase>=2.0.0 (from -r requirements.txt (line 2))
  Downloading supabase-2.28.3-py3-none-any.whl.metadata (4.6 kB)
Collecting beautifulsoup4>=4.12.0 (from -r requirements.txt (line 3))
  Downloading beautifulsoup4-4.14.3-py3-none-any.whl.metadata (3.8 kB)
Collecting requests>=2.31.0 (from -r requirements.txt (line 4))
  Downloading requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)
Collecting httpx>=0.27.0 (from -r requirements.txt (line 5))
  Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting apscheduler>=3.10.0 (from -r requirements.txt (line 6))
  Downloading apscheduler-3.11.2-py3-none-any.whl.metadata (6.4 kB)
Collecting pydantic>=2.0.0 (from -r requirements.txt (line 7))
  Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
Collecting python-dotenv>=1.0.0 (from -r requirements.txt (line 8))
  Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Collecting tenacity>=8.2.0 (from -r requirements.txt (line 9))
  Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
Collecting structlog>=24.0.0 (from -r requirements.txt (line 10))
  Downloading structlog-25.5.0-py3-none-any.whl.metadata (9.5 kB)
Collecting pytest>=8.0.0 (from -r requirements.txt (line 11))
  Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)
Collecting pytest-asyncio>=0.23.0 (from -r requirements.txt (line 12))
  Downloading pytest_asyncio-1.3.0-py3-none-any.whl.metadata (4.1 kB)
Collecting uvicorn>=0.30.0 (from -r requirements.txt (line 13))
  Downloading uvicorn-0.44.0-py3-none-any.whl.metadata (6.7 kB)
Collecting starlette>=0.38.0 (from -r requirements.txt (line 14))
  Downloading starlette-1.0.0-py3-none-any.whl.metadata (6.3 kB)
Collecting python-dateutil>=2.8.2 (from -r requirements.txt (line 15))
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting fastmcp>=0.1.0 (from -r requirements.txt (line 16))
  Downloading fastmcp-3.2.3-py3-none-any.whl.metadata (8.2 kB)
Collecting fastapi>=0.110.0 (from -r requirements.txt (line 17))
  Downloading fastapi-0.135.3-py3-none-any.whl.metadata (28 kB)
Collecting brotlipy (from -r requirements.txt (line 18))
  Downloading brotlipy-0.7.0-cp35-abi3-manylinux2010_x86_64.whl.metadata (2.9 kB)
Collecting docopt (from -r requirements.txt (line 19))
  Downloading docopt-0.6.2.tar.gz (25 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting openpyxl (from -r requirements.txt (line 20))
  Downloading openpyxl-3.1.5-py2.py3-none-any.whl.metadata (2.5 kB)
Collecting pandas (from -r requirements.txt (line 21))
  Downloading pandas-3.0.2-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
Collecting PyYAML (from -r requirements.txt (line 22))
  Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
Collecting rich (from -r requirements.txt (line 23))
  Downloading rich-14.3.4-py3-none-any.whl.metadata (18 kB)
Collecting urllib3 (from -r requirements.txt (line 24))
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting anyio>=4.5 (from mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
Collecting httpx-sse>=0.4 (from mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading httpx_sse-0.4.3-py3-none-any.whl.metadata (9.7 kB)
Collecting jsonschema>=4.20.0 (from mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting pydantic-settings>=2.5.2 (from mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading pydantic_settings-2.13.1-py3-none-any.whl.metadata (3.4 kB)
Collecting pyjwt>=2.10.1 (from pyjwt[crypto]>=2.10.1->mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading pyjwt-2.12.1-py3-none-any.whl.metadata (4.1 kB)
Collecting python-multipart>=0.0.9 (from mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading python_multipart-0.0.26-py3-none-any.whl.metadata (2.1 kB)
Collecting sse-starlette>=1.6.1 (from mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading sse_starlette-3.3.4-py3-none-any.whl.metadata (14 kB)
Collecting typing-extensions>=4.9.0 (from mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting typing-inspection>=0.4.1 (from mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.0.0->-r requirements.txt (line 7))
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.41.5 (from pydantic>=2.0.0->-r requirements.txt (line 7))
  Downloading pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
Collecting realtime==2.28.3 (from supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading realtime-2.28.3-py3-none-any.whl.metadata (7.0 kB)
Collecting supabase-functions==2.28.3 (from supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading supabase_functions-2.28.3-py3-none-any.whl.metadata (2.4 kB)
Collecting storage3==2.28.3 (from supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading storage3-2.28.3-py3-none-any.whl.metadata (2.1 kB)
Collecting supabase-auth==2.28.3 (from supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading supabase_auth-2.28.3-py3-none-any.whl.metadata (6.4 kB)
Collecting postgrest==2.28.3 (from supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading postgrest-2.28.3-py3-none-any.whl.metadata (3.4 kB)
Collecting yarl>=1.22.0 (from supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading yarl-1.23.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
Collecting deprecation>=2.1.0 (from postgrest==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
Collecting websockets<16,>=11 (from realtime==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading websockets-15.0.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
Collecting pyiceberg>=0.10.0 (from storage3==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading pyiceberg-0.11.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.8 kB)
Collecting strenum>=0.4.15 (from supabase-functions==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading StrEnum-0.4.15-py3-none-any.whl.metadata (5.3 kB)
Collecting certifi (from httpx>=0.27.0->-r requirements.txt (line 5))
  Downloading certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
Collecting httpcore==1.* (from httpx>=0.27.0->-r requirements.txt (line 5))
  Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting idna (from httpx>=0.27.0->-r requirements.txt (line 5))
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx>=0.27.0->-r requirements.txt (line 5))
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting h2<5,>=3 (from httpx[http2]<0.29,>=0.26->postgrest==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading h2-4.3.0-py3-none-any.whl.metadata (5.1 kB)
Collecting hyperframe<7,>=6.1 (from h2<5,>=3->httpx[http2]<0.29,>=0.26->postgrest==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading hyperframe-6.1.0-py3-none-any.whl.metadata (4.3 kB)
Collecting hpack<5,>=4.1 (from h2<5,>=3->httpx[http2]<0.29,>=0.26->postgrest==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading hpack-4.1.0-py3-none-any.whl.metadata (4.6 kB)
Collecting soupsieve>=1.6.1 (from beautifulsoup4>=4.12.0->-r requirements.txt (line 3))
  Downloading soupsieve-2.8.3-py3-none-any.whl.metadata (4.6 kB)
Collecting charset_normalizer<4,>=2 (from requests>=2.31.0->-r requirements.txt (line 4))
  Downloading charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
Collecting tzlocal>=3.0 (from apscheduler>=3.10.0->-r requirements.txt (line 6))
  Downloading tzlocal-5.3.1-py3-none-any.whl.metadata (7.6 kB)
Collecting iniconfig>=1.0.1 (from pytest>=8.0.0->-r requirements.txt (line 11))
  Downloading iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
Collecting packaging>=22 (from pytest>=8.0.0->-r requirements.txt (line 11))
  Downloading packaging-26.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest>=8.0.0->-r requirements.txt (line 11))
  Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting pygments>=2.7.2 (from pytest>=8.0.0->-r requirements.txt (line 11))
  Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Collecting click>=7.0 (from uvicorn>=0.30.0->-r requirements.txt (line 13))
  Downloading click-8.3.2-py3-none-any.whl.metadata (2.6 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->-r requirements.txt (line 15))
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting authlib>=1.6.5 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading authlib-1.6.9-py2.py3-none-any.whl.metadata (9.8 kB)
Collecting cyclopts>=4.0.0 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading cyclopts-4.10.2-py3-none-any.whl.metadata (12 kB)
Collecting exceptiongroup>=1.2.2 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading exceptiongroup-1.3.1-py3-none-any.whl.metadata (6.7 kB)
Collecting jsonref>=1.1.0 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading jsonref-1.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting jsonschema-path>=0.3.4 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading jsonschema_path-0.4.5-py3-none-any.whl.metadata (5.9 kB)
Collecting openapi-pydantic>=0.5.1 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading openapi_pydantic-0.5.1-py3-none-any.whl.metadata (10 kB)
Collecting opentelemetry-api>=1.20.0 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading opentelemetry_api-1.41.0-py3-none-any.whl.metadata (1.5 kB)
Collecting platformdirs>=4.0.0 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading platformdirs-4.9.6-py3-none-any.whl.metadata (4.7 kB)
Collecting py-key-value-aio<0.5.0,>=0.4.4 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading py_key_value_aio-0.4.4-py3-none-any.whl.metadata (15 kB)
Collecting pyperclip>=1.9.0 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading pyperclip-1.11.0-py3-none-any.whl.metadata (2.4 kB)
Collecting uncalled-for>=0.2.0 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading uncalled_for-0.3.1-py3-none-any.whl.metadata (2.9 kB)
Collecting watchfiles>=1.0.0 (from fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading watchfiles-1.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting beartype>=0.20.0 (from py-key-value-aio<0.5.0,>=0.4.4->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading beartype-0.22.9-py3-none-any.whl.metadata (37 kB)
Collecting aiofile>=3.5.0 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading aiofile-3.9.0-py3-none-any.whl.metadata (14 kB)
Collecting keyring>=25.6.0 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading keyring-25.7.0-py3-none-any.whl.metadata (21 kB)
Collecting cachetools>=5.0.0 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading cachetools-7.0.5-py3-none-any.whl.metadata (5.6 kB)
Collecting annotated-doc>=0.0.2 (from fastapi>=0.110.0->-r requirements.txt (line 17))
  Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Collecting cffi>=1.0.0 (from brotlipy->-r requirements.txt (line 18))
  Downloading cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
Collecting et-xmlfile (from openpyxl->-r requirements.txt (line 20))
  Downloading et_xmlfile-2.0.0-py3-none-any.whl.metadata (2.7 kB)
Collecting numpy>=1.26.0 (from pandas->-r requirements.txt (line 21))
  Downloading numpy-2.4.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting markdown-it-py>=2.2.0 (from rich->-r requirements.txt (line 23))
  Downloading markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)
Collecting caio<0.10.0,>=0.9.0 (from aiofile>=3.5.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading caio-0.9.25-cp311-cp311-manylinux_2_34_x86_64.whl.metadata (3.3 kB)
Collecting cryptography (from authlib>=1.6.5->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading cryptography-46.0.7-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
Collecting pycparser (from cffi>=1.0.0->brotlipy->-r requirements.txt (line 18))
  Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Collecting attrs>=23.1.0 (from cyclopts>=4.0.0->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting docstring-parser<4.0,>=0.15 (from cyclopts>=4.0.0->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading docstring_parser-0.17.0-py3-none-any.whl.metadata (3.5 kB)
Collecting rich-rst<2.0.0,>=1.3.1 (from cyclopts>=4.0.0->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading rich_rst-1.3.2-py3-none-any.whl.metadata (6.1 kB)
Collecting docutils (from rich-rst<2.0.0,>=1.3.1->cyclopts>=4.0.0->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading docutils-0.22.4-py3-none-any.whl.metadata (15 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.20.0->mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=4.20.0->mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=4.20.0->mcp>=1.0.0->-r requirements.txt (line 1))
  Downloading rpds_py-0.30.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
Collecting pathable<0.6.0,>=0.5.0 (from jsonschema-path>=0.3.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading pathable-0.5.0-py3-none-any.whl.metadata (5.9 kB)
Collecting SecretStorage>=3.2 (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading secretstorage-3.5.0-py3-none-any.whl.metadata (4.0 kB)
Collecting jeepney>=0.4.2 (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading jeepney-0.9.0-py3-none-any.whl.metadata (1.2 kB)
Collecting importlib_metadata>=4.11.4 (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading importlib_metadata-9.0.0-py3-none-any.whl.metadata (4.5 kB)
Collecting jaraco.classes (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
Collecting jaraco.functools (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading jaraco_functools-4.4.0-py3-none-any.whl.metadata (3.0 kB)
Collecting jaraco.context (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading jaraco_context-6.1.2-py3-none-any.whl.metadata (4.2 kB)
Collecting zipp>=3.20 (from importlib_metadata>=4.11.4->keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading zipp-3.23.0-py3-none-any.whl.metadata (3.6 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich->-r requirements.txt (line 23))
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting importlib_metadata>=4.11.4 (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading importlib_metadata-8.7.1-py3-none-any.whl.metadata (4.7 kB)
Collecting email-validator>=2.0.0 (from pydantic[email]>=2.11.7->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading email_validator-2.3.0-py3-none-any.whl.metadata (26 kB)
Collecting dnspython>=2.0.0 (from email-validator>=2.0.0->pydantic[email]>=2.11.7->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading dnspython-2.8.0-py3-none-any.whl.metadata (5.7 kB)
Collecting mmh3<6.0.0,>=4.0.0 (from pyiceberg>=0.10.0->storage3==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading mmh3-5.2.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (14 kB)
Collecting strictyaml<2.0.0,>=1.7.0 (from pyiceberg>=0.10.0->storage3==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading strictyaml-1.7.3-py3-none-any.whl.metadata (11 kB)
Collecting fsspec>=2023.1.0 (from pyiceberg>=0.10.0->storage3==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading fsspec-2026.3.0-py3-none-any.whl.metadata (10 kB)
Collecting pyparsing<4.0.0,>=3.1.0 (from pyiceberg>=0.10.0->storage3==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Collecting pyroaring<2.0.0,>=1.0.0 (from pyiceberg>=0.10.0->storage3==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading pyroaring-1.0.4-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (11 kB)
Collecting cachetools>=5.0.0 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading cachetools-6.2.6-py3-none-any.whl.metadata (5.6 kB)
Collecting zstandard<1.0.0,>=0.13.0 (from pyiceberg>=0.10.0->storage3==2.28.3->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading zstandard-0.25.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (3.3 kB)
Collecting multidict>=4.0 (from yarl>=1.22.0->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading multidict-6.7.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting propcache>=0.2.1 (from yarl>=1.22.0->supabase>=2.0.0->-r requirements.txt (line 2))
  Downloading propcache-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (13 kB)
Collecting more-itertools (from jaraco.classes->keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading more_itertools-11.0.2-py3-none-any.whl.metadata (41 kB)
Collecting backports.tarfile (from jaraco.context->keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4->fastmcp>=0.1.0->-r requirements.txt (line 16))
  Downloading backports.tarfile-1.2.0-py3-none-any.whl.metadata (2.0 kB)
Downloading mcp-1.27.0-py3-none-any.whl (215 kB)
Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
Downloading pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 58.9 MB/s  0:00:00
Downloading supabase-2.28.3-py3-none-any.whl (16 kB)
Downloading postgrest-2.28.3-py3-none-any.whl (21 kB)
Downloading realtime-2.28.3-py3-none-any.whl (22 kB)
Downloading storage3-2.28.3-py3-none-any.whl (28 kB)
Downloading supabase_auth-2.28.3-py3-none-any.whl (48 kB)
Downloading supabase_functions-2.28.3-py3-none-any.whl (8.8 kB)
Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
Downloading h2-4.3.0-py3-none-any.whl (61 kB)
Downloading hpack-4.1.0-py3-none-any.whl (34 kB)
Downloading hyperframe-6.1.0-py3-none-any.whl (13 kB)
Downloading websockets-15.0.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
Downloading beautifulsoup4-4.14.3-py3-none-any.whl (107 kB)
Downloading requests-2.33.1-py3-none-any.whl (64 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (214 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading apscheduler-3.11.2-py3-none-any.whl (64 kB)
Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)
Downloading structlog-25.5.0-py3-none-any.whl (72 kB)
Downloading pytest-9.0.3-py3-none-any.whl (375 kB)
Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
Downloading pytest_asyncio-1.3.0-py3-none-any.whl (15 kB)
Downloading uvicorn-0.44.0-py3-none-any.whl (69 kB)
Downloading starlette-1.0.0-py3-none-any.whl (72 kB)
Downloading anyio-4.13.0-py3-none-any.whl (114 kB)
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading fastmcp-3.2.3-py3-none-any.whl (707 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 707.3/707.3 kB 129.0 MB/s  0:00:00
Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (806 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 806.6/806.6 kB 167.0 MB/s  0:00:00
Downloading py_key_value_aio-0.4.4-py3-none-any.whl (152 kB)
Downloading fastapi-0.135.3-py3-none-any.whl (117 kB)
Downloading brotlipy-0.7.0-cp35-abi3-manylinux2010_x86_64.whl (1.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 180.9 MB/s  0:00:00
Downloading openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
Downloading pandas-3.0.2-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (11.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.3/11.3 MB 180.6 MB/s  0:00:00
Downloading rich-14.3.4-py3-none-any.whl (310 kB)
Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 182.4 MB/s  0:00:00
Downloading aiofile-3.9.0-py3-none-any.whl (19 kB)
Downloading caio-0.9.25-cp311-cp311-manylinux_2_34_x86_64.whl (78 kB)
Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading authlib-1.6.9-py2.py3-none-any.whl (244 kB)
Downloading beartype-0.22.9-py3-none-any.whl (1.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 234.6 MB/s  0:00:00
Downloading certifi-2026.2.25-py3-none-any.whl (153 kB)
Downloading cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (215 kB)
Downloading click-8.3.2-py3-none-any.whl (108 kB)
Downloading cyclopts-4.10.2-py3-none-any.whl (204 kB)
Downloading docstring_parser-0.17.0-py3-none-any.whl (36 kB)
Downloading rich_rst-1.3.2-py3-none-any.whl (12 kB)
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
Downloading exceptiongroup-1.3.1-py3-none-any.whl (16 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading httpx_sse-0.4.3-py3-none-any.whl (9.0 kB)
Downloading iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
Downloading jsonref-1.1.0-py3-none-any.whl (9.4 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Downloading jsonschema_path-0.4.5-py3-none-any.whl (19 kB)
Downloading pathable-0.5.0-py3-none-any.whl (16 kB)
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading keyring-25.7.0-py3-none-any.whl (39 kB)
Downloading jeepney-0.9.0-py3-none-any.whl (49 kB)
Downloading markdown_it_py-4.0.0-py3-none-any.whl (87 kB)
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading numpy-2.4.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.9/16.9 MB 305.9 MB/s  0:00:00
Downloading openapi_pydantic-0.5.1-py3-none-any.whl (96 kB)
Downloading opentelemetry_api-1.41.0-py3-none-any.whl (69 kB)
Downloading importlib_metadata-8.7.1-py3-none-any.whl (27 kB)
Downloading packaging-26.0-py3-none-any.whl (74 kB)
Downloading platformdirs-4.9.6-py3-none-any.whl (21 kB)
Downloading pydantic_settings-2.13.1-py3-none-any.whl (58 kB)
Downloading email_validator-2.3.0-py3-none-any.whl (35 kB)
Downloading dnspython-2.8.0-py3-none-any.whl (331 kB)
Downloading pyiceberg-0.11.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (721 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 721.2/721.2 kB 145.8 MB/s  0:00:00
Downloading cachetools-6.2.6-py3-none-any.whl (11 kB)
Downloading mmh3-5.2.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (103 kB)
Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
Downloading pyroaring-1.0.4-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 256.5 MB/s  0:00:00
Downloading strictyaml-1.7.3-py3-none-any.whl (123 kB)
Downloading zstandard-0.25.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (5.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 320.3 MB/s  0:00:00
Downloading fsspec-2026.3.0-py3-none-any.whl (202 kB)
Downloading pyjwt-2.12.1-py3-none-any.whl (29 kB)
Downloading cryptography-46.0.7-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 332.7 MB/s  0:00:00
Downloading pyperclip-1.11.0-py3-none-any.whl (11 kB)
Downloading python_multipart-0.0.26-py3-none-any.whl (28 kB)
Downloading rpds_py-0.30.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (390 kB)
Downloading secretstorage-3.5.0-py3-none-any.whl (15 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading soupsieve-2.8.3-py3-none-any.whl (37 kB)
Downloading sse_starlette-3.3.4-py3-none-any.whl (14 kB)
Downloading StrEnum-0.4.15-py3-none-any.whl (8.9 kB)
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Downloading tzlocal-5.3.1-py3-none-any.whl (18 kB)
Downloading uncalled_for-0.3.1-py3-none-any.whl (11 kB)
Downloading watchfiles-1.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
Downloading yarl-1.23.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (102 kB)
Downloading multidict-6.7.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (246 kB)
Downloading propcache-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (210 kB)
Downloading zipp-3.23.0-py3-none-any.whl (10 kB)
Downloading docutils-0.22.4-py3-none-any.whl (633 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 633.2/633.2 kB 116.7 MB/s  0:00:00
Downloading et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
Downloading jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
Downloading jaraco_context-6.1.2-py3-none-any.whl (7.9 kB)
Downloading backports.tarfile-1.2.0-py3-none-any.whl (30 kB)
Downloading jaraco_functools-4.4.0-py3-none-any.whl (10 kB)
Downloading more_itertools-11.0.2-py3-none-any.whl (71 kB)
Downloading pycparser-3.0-py3-none-any.whl (48 kB)
Building wheels for collected packages: docopt
  Building wheel for docopt (pyproject.toml): started
  Building wheel for docopt (pyproject.toml): finished with status 'done'
  Created wheel for docopt: filename=docopt-0.6.2-py2.py3-none-any.whl size=13782 sha256=261c842985573b00ad22a38636a80b1f5669d48a1b8ec5606b9b6dd16c5e9901
  Stored in directory: /home/runner/.cache/pip/wheels/1a/b0/8c/4b75c4116c31f83c8f9f047231251e13cc74481cca4a78a9ce
Successfully built docopt
Installing collected packages: strenum, pyroaring, pyperclip, docopt, zstandard, zipp, websockets, urllib3, uncalled-for, tzlocal, typing-extensions, tenacity, structlog, soupsieve, six, rpds-py, PyYAML, python-multipart, python-dotenv, pyparsing, pyjwt, pygments, pycparser, propcache, pluggy, platformdirs, pathable, packaging, numpy, multidict, more-itertools, mmh3, mdurl, jsonref, jeepney, iniconfig, idna, hyperframe, httpx-sse, hpack, h11, fsspec, et-xmlfile, docutils, docstring-parser, dnspython, click, charset_normalizer, certifi, caio, cachetools, beartype, backports.tarfile, attrs, annotated-types, annotated-doc, yarl, uvicorn, typing-inspection, requests, referencing, python-dateutil, pytest, pydantic-core, py-key-value-aio, openpyxl, markdown-it-py, jaraco.functools, jaraco.context, jaraco.classes, importlib_metadata, httpcore, h2, exceptiongroup, email-validator, deprecation, cffi, beautifulsoup4, apscheduler, anyio, aiofile, watchfiles, strictyaml, starlette, rich, pytest-asyncio, pydantic, pandas,
Successfully installed PyYAML-6.0.3 SecretStorage-3.5.0 aiofile-3.9.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.13.0 apscheduler-3.11.2 attrs-26.1.0 authlib-1.6.9 backports.tarfile-1.2.0 beartype-0.22.9 beautifulsoup4-4.14.3 brotlipy-0.7.0 cachetools-6.2.6 caio-0.9.25 certifi-2026.2.25 cffi-2.0.0 charset_normalizer-3.4.7 click-8.3.2 cryptography-46.0.7 cyclopts-4.10.2 deprecation-2.1.0 dnspython-2.8.0 docopt-0.6.2 docstring-parser-0.17.0 docutils-0.22.4 email-validator-2.3.0 et-xmlfile-2.0.0 exceptiongroup-1.3.1 fastapi-0.135.3 fastmcp-3.2.3 fsspec-2026.3.0 h11-0.16.0 h2-4.3.0 hpack-4.1.0 httpcore-1.0.9 httpx-0.28.1 httpx-sse-0.4.3 hyperframe-6.1.0 idna-3.11 importlib_metadata-8.7.1 iniconfig-2.3.0 jaraco.classes-3.4.0 jaraco.context-6.1.2 jaraco.functools-4.4.0 jeepney-0.9.0 jsonref-1.1.0 jsonschema-4.26.0 jsonschema-path-0.4.5 jsonschema-specifications-2025.9.1 keyring-25.7.0 markdown-it-py-4.0.0 mcp-1.27.0 mdurl-0.1.2 mmh3-5.2.1 more-itertools-11.0.2 multidict-6.7.1 numpy-2.4.4 openapi-pydantic-0.5
5m 41s
Run # Set the PYTHONPATH so the src modules are properly found
  
🚀 Starting GitHub Actions Daily Scraper
📊 Pre-scrape Health Report:
    ] job_start                      job=health_report
    ] supabase_client_initialized
    ] health_report                  alerts=None avg_data_age_hours=124.5 counts={'scholarships': 6399, 'courses': 153648, 'universities': 1185, 'visa_requirements': 60, 'cost_of_living': 23}
    ] job_complete                   counts={'scholarships': 6399, 'courses': 153648, 'universities': 1185, 'visa_requirements': 60, 'cost_of_living': 23} elapsed_seconds=5.5 job=health_report
🌐 Running All live scrapers and syncing to Supabase...
    ] job_start                      job=scrape_all_databases
    ] group_start                    group=heavy scrapers=['scholarships', 'courses', 'universities']
    ] checkpoint_loaded              completed=18 scraper=IDPCourseScraper
    ] scrape_start                   max_concurrent=8 rate_limit=0.15 scraper=IDPScholarshipScraper total_combos=36
    ] checkpoint_cleared             scraper=idp_courses
    ] scrape_start                   max_concurrent=10 rate_limit=0.1 scraper=IDPCourseScraper total_combos=18
    ] phase1_start                   description='Collecting university URLs from listing pages' scraper=IDPUniversityScraper
    ] combo_start                    combo=australia:undergraduate elapsed=0.0s progress=0.0% scraper=IDPScholarshipScraper
    ] combo_start                    combo=australia:postgraduate elapsed=0.0s progress=2.8% scraper=IDPScholarshipScraper
    ] combo_start                    combo=australia:doctorate elapsed=0.0s progress=5.6% scraper=IDPScholarshipScraper
    ] combo_start                    combo=australia:foundation elapsed=0.0s progress=8.3% scraper=IDPScholarshipScraper
    ] combo_start                    combo=australia:pre-degree-vocational elapsed=0.0s progress=11.1% scraper=IDPScholarshipScraper
    ] combo_start                    combo=australia:school elapsed=0.0s progress=13.9% scraper=IDPScholarshipScraper
    ] combo_start                    combo=uk:undergraduate elapsed=0.0s progress=16.7% scraper=IDPScholarshipScraper
    ] combo_start                    combo=uk:postgraduate elapsed=0.0s progress=19.4% scraper=IDPScholarshipScraper
    ] combo_start                    combo=australia:undergraduate elapsed=0.0s progress=0.0% scraper=IDPCourseScraper
    ] combo_start                    combo=australia:postgraduate elapsed=0.0s progress=5.6% scraper=IDPCourseScraper
    ] combo_start                    combo=australia:doctorate elapsed=0.0s progress=11.1% scraper=IDPCourseScraper
    ] combo_start                    combo=united-kingdom:undergraduate elapsed=0.0s progress=16.7% scraper=IDPCourseScraper
    ] combo_start                    combo=united-kingdom:postgraduate elapsed=0.0s progress=22.2% scraper=IDPCourseScraper
    ] combo_start                    combo=united-kingdom:doctorate elapsed=0.0s progress=27.8% scraper=IDPCourseScraper
    ] combo_start                    combo=canada:undergraduate elapsed=0.0s progress=33.3% scraper=IDPCourseScraper
    ] combo_start                    combo=canada:postgraduate elapsed=0.0s progress=38.9% scraper=IDPCourseScraper
    ] combo_start                    combo=canada:doctorate elapsed=0.0s progress=44.4% scraper=IDPCourseScraper
    ] combo_start                    combo=united-states:undergraduate elapsed=0.0s progress=50.0% scraper=IDPCourseScraper
    ] http_request                   response_time_ms=89.4 scraper=IDPCourseScraper status_code=200 url=https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/
    ] http_request                   response_time_ms=31.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=3'
    ] http_request                   response_time_ms=31.0 scraper=IDPCourseScraper status_code=200 url=https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/
    ] http_request                   response_time_ms=40.5 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=postgraduate'
    ] http_request                   response_time_ms=1025.5 scraper=IDPCourseScraper status_code=200 url=https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/
    ] http_request                   response_time_ms=984.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=3'
    ] http_request                   response_time_ms=1209.4 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=school'
    ] http_request                   response_time_ms=26.8 scraper=IDPCourseScraper status_code=200 url=https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/
    ] http_request                   response_time_ms=1579.0 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=doctorate'
    ] http_request                   response_time_ms=23.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/master-of-applied-engineering-(mappe)-bursary/154183/
    ] http_request                   response_time_ms=1552.0 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=undergraduate'
    ] http_request                   response_time_ms=1849.4 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=1'
    ] http_request                   response_time_ms=20.3 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=2'
    ] http_request                   response_time_ms=1538.3 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=pre-degree-vocational'
    ] http_request                   response_time_ms=1010.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=2'
    ] http_request                   response_time_ms=1129.0 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=undergraduate'
    ] total_pages_detected           combo=australia:doctorate estimated_courses=1212 scraper=IDPCourseScraper total_pages=101
    ] http_request                   response_time_ms=954.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-high-achiever-award/121563/
    ] http_request                   response_time_ms=813.0 scraper=IDPCourseScraper status_code=200 url=https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/
    ] http_request                   response_time_ms=1970.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=2'
    ] http_request                   response_time_ms=2373.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=2'
    ] http_request                   response_time_ms=1393.0 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=foundation'
    ] http_request                   response_time_ms=937.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-english-distinction-award/70793/
    ] http_request                   response_time_ms=1847.4 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=postgraduate'
    ] http_request                   response_time_ms=831.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/top-achiever-scholarships/110570/
    ] http_request                   response_time_ms=65.7 scraper=IDPCourseScraper status_code=200 url=https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/
    ] http_request                   response_time_ms=67.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/school-of-social-work-and-social-policy-international-postgraduate-taught-scholarship/166837/
    ] http_request                   response_time_ms=2081.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=3'
    ] http_request                   response_time_ms=23.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/global-scholarship/166278/
    ] http_request                   response_time_ms=19.1 scraper=IDPCourseScraper status_code=200 url=https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/
    ] http_request                   response_time_ms=1701.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-communication-distinction-award/25602/
    ] http_request                   response_time_ms=1967.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=3'
    ] total_pages_detected           combo=australia:undergraduate estimated_courses=13164 scraper=IDPCourseScraper total_pages=1097
    ] http_request                   response_time_ms=2085.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=2'
    ] http_request                   response_time_ms=822.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/global-excellence-undergraduate-scholarships/129919/
    ] http_request                   response_time_ms=2490.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=2'
    ] http_request                   response_time_ms=2389.7 scraper=IDPCourseScraper status_code=200 url=https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/
    ] http_request                   response_time_ms=235.0 scraper=IDPCourseScraper status_code=200 url=https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/
    ] total_pages_detected           combo=canada:postgraduate estimated_courses=5640 scraper=IDPCourseScraper total_pages=470
    ] http_request                   response_time_ms=2303.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=3'
    ] http_request                   response_time_ms=2001.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=3'
    ] total_pages_detected           combo=united-kingdom:postgraduate estimated_courses=19104 scraper=IDPCourseScraper total_pages=1592
    ] http_request                   response_time_ms=216.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/undergraduate-academic-scholarships/152222/
    ] http_request                   response_time_ms=165.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-communication-distinction-award/25602/
    ] http_request                   response_time_ms=382.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=3'
    ] total_pages_detected           combo=canada:undergraduate estimated_courses=13260 scraper=IDPCourseScraper total_pages=1105
    ] http_request                   response_time_ms=85.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-high-achiever-award/121563/
    ] http_request                   response_time_ms=2309.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=2'
    ] http_request                   response_time_ms=2337.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=2'
    ] http_request                   response_time_ms=1780.2 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=3'
    ] http_request                   response_time_ms=2236.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-for-non-ucd-students-graduates/148208/
    ] total_pages_detected           combo=australia:postgraduate estimated_courses=7908 scraper=IDPCourseScraper total_pages=659
    ] http_request                   response_time_ms=159.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/master-of-applied-engineering-(mappe)-bursary/154183/
    ] http_request                   response_time_ms=44.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-english-distinction-award/70793/
    ] http_request                   response_time_ms=2063.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=3'
    ] http_request                   response_time_ms=1654.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/faculty-of-engineering-computing-international-scholarship/161080/
    ] http_request                   response_time_ms=87.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=4'
    ] http_request                   response_time_ms=12.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/top-achiever-scholarships/110570/
    ] http_request                   response_time_ms=2714.8 scraper=IDPCourseScraper status_code=200 url=https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/
    ] total_pages_detected           combo=canada:doctorate estimated_courses=1980 scraper=IDPCourseScraper total_pages=165
    ] http_request                   response_time_ms=2163.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=2'
    ] http_request                   response_time_ms=2609.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=2'
    ] http_request                   response_time_ms=1964.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=2'
    ] total_pages_detected           combo=united-kingdom:undergraduate estimated_courses=32580 scraper=IDPCourseScraper total_pages=2715
    ] http_request                   response_time_ms=150.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-for-non-ucd-students-graduates/148208/
    ] http_request                   response_time_ms=1805.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/dr-jonathan-ks-chiu-and-dr-margaret-sau-sheung-ip-undergraduate-scholarship/161386/
    ] http_request                   response_time_ms=1695.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=3'
    ] total_pages_detected           combo=united-states:undergraduate estimated_courses=49980 scraper=IDPCourseScraper total_pages=4165
    ] http_request                   response_time_ms=131.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/global-excellence-undergraduate-scholarships/129919/
    ] http_request                   response_time_ms=2220.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=3'
    ] http_request                   response_time_ms=1064.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=6'
    ] total_pages_detected           combo=united-kingdom:doctorate estimated_courses=5184 scraper=IDPCourseScraper total_pages=432
    ] http_request                   response_time_ms=95.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/school-of-social-work-and-social-policy-international-postgraduate-taught-scholarship/166837/
    ] http_request                   response_time_ms=12.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/global-scholarship/166278/
    ] http_request                   response_time_ms=11.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/faculty-of-engineering-computing-international-scholarship/161080/
    ] http_request                   response_time_ms=2268.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=4'
    ] http_request                   response_time_ms=12.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/dr-jonathan-ks-chiu-and-dr-margaret-sau-sheung-ip-undergraduate-scholarship/161386/
    ] http_request                   response_time_ms=1922.0 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=4'
    ] http_request                   response_time_ms=10.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/undergraduate-academic-scholarships/152222/
    ] http_request                   response_time_ms=11.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-communication-distinction-award/25602/
    ] http_request                   response_time_ms=741.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=4'
    ] http_request                   response_time_ms=10.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-high-achiever-award/121563/
    ] http_request                   response_time_ms=58.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=5'
    ] http_request                   response_time_ms=2594.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=5'
    ] http_request                   response_time_ms=511.0 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=5'
    ] http_request                   response_time_ms=2241.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=5'
    ] http_request                   response_time_ms=162.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/master-of-applied-engineering-(mappe)-bursary/154183/
    ] http_request                   response_time_ms=35.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-english-distinction-award/70793/
    ] http_request                   response_time_ms=84.4 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=6'
    ] http_request                   response_time_ms=11.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/top-achiever-scholarships/110570/
    ] http_request                   response_time_ms=2326.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=6'
    ] http_request                   response_time_ms=2306.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=4'
    ] http_request                   response_time_ms=2107.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=5'
    ] http_request                   response_time_ms=137.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-for-non-ucd-students-graduates/148208/
    ] http_request                   response_time_ms=11.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/global-excellence-undergraduate-scholarships/129919/
    ] http_request                   response_time_ms=1192.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=6'
    ] http_request                   response_time_ms=9.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/school-of-social-work-and-social-policy-international-postgraduate-taught-scholarship/166837/
    ] http_request                   response_time_ms=2173.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=6'
    ] http_request                   response_time_ms=9.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/global-scholarship/166278/
    ] http_request                   response_time_ms=1884.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=5'
    ] http_request                   response_time_ms=1872.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=6'
    ] http_request                   response_time_ms=12.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/faculty-of-engineering-computing-international-scholarship/161080/
    ] http_request                   response_time_ms=1966.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=5'
    ] http_request                   response_time_ms=11.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/dr-jonathan-ks-chiu-and-dr-margaret-sau-sheung-ip-undergraduate-scholarship/161386/
    ] http_request                   response_time_ms=2190.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=4'
    ] http_request                   response_time_ms=2010.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=4'
    ] http_request                   response_time_ms=13.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/undergraduate-academic-scholarships/152222/
    ] http_request                   response_time_ms=11.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-communication-distinction-award/25602/
    ] http_request                   response_time_ms=11.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-high-achiever-award/121563/
    ] http_request                   response_time_ms=944.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=5'
    ] http_request                   response_time_ms=2180.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=6'
    ] http_request                   response_time_ms=2116.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=4'
    ] http_request                   response_time_ms=1816.9 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=7'
    ] http_request                   response_time_ms=42.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/master-of-applied-engineering-(mappe)-bursary/154183/
    ] http_request                   response_time_ms=10.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-english-distinction-award/70793/
    ] http_request                   response_time_ms=1023.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=4'
    ] http_request                   response_time_ms=2206.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=5'
    ] http_request                   response_time_ms=1816.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=5'
    ] http_request                   response_time_ms=2035.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=4'
    ] http_request                   response_time_ms=904.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=5'
    ] http_request                   response_time_ms=11.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/top-achiever-scholarships/110570/
    ] http_request                   response_time_ms=9.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-for-non-ucd-students-graduates/148208/
    ] http_request                   response_time_ms=1166.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=6'
    ] http_request                   response_time_ms=2000.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=4'
    ] http_request                   response_time_ms=624.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=7'
    ] http_request                   response_time_ms=2666.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=6'
    ] http_request                   response_time_ms=135.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/global-excellence-undergraduate-scholarships/129919/
    ] http_request                   response_time_ms=336.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=8'
    ] http_request                   response_time_ms=2535.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=6'
    ] http_request                   response_time_ms=124.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/school-of-social-work-and-social-policy-international-postgraduate-taught-scholarship/166837/
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/global-scholarship/166278/
    ] http_request                   response_time_ms=1254.3 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=8'
    ] http_request                   response_time_ms=8.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/faculty-of-engineering-computing-international-scholarship/161080/
    ] http_request                   response_time_ms=1930.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=7'
    ] http_request                   response_time_ms=2606.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=6'
    ] http_request                   response_time_ms=139.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/dr-jonathan-ks-chiu-and-dr-margaret-sau-sheung-ip-undergraduate-scholarship/161386/
    ] http_request                   response_time_ms=11.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/undergraduate-academic-scholarships/152222/
    ] http_request                   response_time_ms=493.6 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=9'
    ] http_request                   response_time_ms=9.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-communication-distinction-award/25602/
    ] http_request                   response_time_ms=2322.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=8'
    ] http_request                   response_time_ms=11.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-high-achiever-award/121563/
    ] http_request                   response_time_ms=9.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/master-of-applied-engineering-(mappe)-bursary/154183/
    ] http_request                   response_time_ms=2346.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=9'
    ] http_request                   response_time_ms=76.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=7'
    ] http_request                   response_time_ms=617.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=9'
    ] http_request                   response_time_ms=13.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-english-distinction-award/70793/
    ] http_request                   response_time_ms=2379.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=8'
    ] http_request                   response_time_ms=1459.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=8'
    ] http_request                   response_time_ms=10.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/top-achiever-scholarships/110570/
    ] http_request                   response_time_ms=2385.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=9'
    ] http_request                   response_time_ms=11.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-for-non-ucd-students-graduates/148208/
    ] http_request                   response_time_ms=2614.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=7'
    ] http_request                   response_time_ms=2218.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=9'
    ] http_request                   response_time_ms=8.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/global-excellence-undergraduate-scholarships/129919/
    ] http_request                   response_time_ms=226.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=9'
    ] http_request                   response_time_ms=664.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=9'
    ] http_request                   response_time_ms=2009.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=9'
    ] http_request                   response_time_ms=9.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/school-of-social-work-and-social-policy-international-postgraduate-taught-scholarship/166837/
    ] http_request                   response_time_ms=1654.3 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=10'
    ] listing_progress               collected=120 page=10 scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=52.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/global-scholarship/166278/
    ] http_request                   response_time_ms=53.8 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=11'
    ] http_request                   response_time_ms=2594.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=7'
    ] http_request                   response_time_ms=2096.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=8'
    ] http_request                   response_time_ms=2236.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=7'
    ] http_request                   response_time_ms=173.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/faculty-of-engineering-computing-international-scholarship/161080/
    ] http_request                   response_time_ms=2073.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=8'
    ] http_request                   response_time_ms=2174.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=7'
    ] http_request                   response_time_ms=14.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/undergraduate-academic-scholarships/152222/
    ] http_request                   response_time_ms=376.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/dr-jonathan-ks-chiu-and-dr-margaret-sau-sheung-ip-undergraduate-scholarship/161386/
    ] http_request                   response_time_ms=1785.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=8'
    ] http_request                   response_time_ms=2260.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=9'
    ] http_request                   response_time_ms=830.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=8'
    ] http_request                   response_time_ms=131.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-communication-distinction-award/25602/
    ] http_request                   response_time_ms=10.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-high-achiever-award/121563/
    ] http_request                   response_time_ms=9.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/master-of-applied-engineering-(mappe)-bursary/154183/
    ] http_request                   response_time_ms=9.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-english-distinction-award/70793/
    ] http_request                   response_time_ms=2219.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=7'
    ] http_request                   response_time_ms=834.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=10'
    ] http_request                   response_time_ms=2117.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=8'
    ] http_request                   response_time_ms=171.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/top-achiever-scholarships/110570/
    ] http_request                   response_time_ms=1857.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=9'
    ] http_request                   response_time_ms=1959.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=8'
    ] http_request                   response_time_ms=2066.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=7'
    ] http_request                   response_time_ms=167.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-for-non-ucd-students-graduates/148208/
    ] http_request                   response_time_ms=47.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/global-excellence-undergraduate-scholarships/129919/
    ] http_request                   response_time_ms=1973.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=7'
    ] http_request                   response_time_ms=625.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=10'
    ] http_request                   response_time_ms=10.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/school-of-social-work-and-social-policy-international-postgraduate-taught-scholarship/166837/
    ] http_request                   response_time_ms=1199.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=12'
    ] http_request                   response_time_ms=11.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/global-scholarship/166278/
    ] http_request                   response_time_ms=2027.6 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=12'
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/faculty-of-engineering-computing-international-scholarship/161080/
    ] http_request                   response_time_ms=942.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=11'
    ] http_request                   response_time_ms=91.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=11'
    ] http_request                   response_time_ms=8.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/dr-jonathan-ks-chiu-and-dr-margaret-sau-sheung-ip-undergraduate-scholarship/161386/
    ] http_request                   response_time_ms=2055.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=11'
    ] http_request                   response_time_ms=2480.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=9'
    ] http_request                   response_time_ms=246.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/undergraduate-academic-scholarships/152222/
    ] http_request                   response_time_ms=1287.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=12'
    ] http_request                   response_time_ms=222.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-communication-distinction-award/25602/
    ] http_request                   response_time_ms=869.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=12'
    ] http_request                   response_time_ms=58.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-high-achiever-award/121563/
    ] http_request                   response_time_ms=1187.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=10'
    ] http_request                   response_time_ms=236.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/master-of-applied-engineering-(mappe)-bursary/154183/
    ] http_request                   response_time_ms=2592.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=10'
    ] http_request                   response_time_ms=2492.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=11'
    ] http_request                   response_time_ms=42.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-english-distinction-award/70793/
    ] http_request                   response_time_ms=31.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=12'
    ] http_request                   response_time_ms=1813.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=11'
    ] http_request                   response_time_ms=9.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/top-achiever-scholarships/110570/
    ] http_request                   response_time_ms=1992.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=10'
    ] http_request                   response_time_ms=2659.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=12'
    ] http_request                   response_time_ms=10.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-for-non-ucd-students-graduates/148208/
    ] http_request                   response_time_ms=1302.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=10'
    ] http_request                   response_time_ms=1777.1 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=13'
    ] http_request                   response_time_ms=9.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/global-excellence-undergraduate-scholarships/129919/
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/school-of-social-work-and-social-policy-international-postgraduate-taught-scholarship/166837/
    ] http_request                   response_time_ms=9.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/global-scholarship/166278/
    ] http_request                   response_time_ms=1363.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=12'
    ] http_request                   response_time_ms=10.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/faculty-of-engineering-computing-international-scholarship/161080/
    ] http_request                   response_time_ms=29.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=15'
    ] http_request                   response_time_ms=9.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/dr-jonathan-ks-chiu-and-dr-margaret-sau-sheung-ip-undergraduate-scholarship/161386/
    ] http_request                   response_time_ms=2769.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=12'
    ] http_request                   response_time_ms=1059.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=12'
    ] http_request                   response_time_ms=1160.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=11'
    ] http_request                   response_time_ms=1008.7 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=14'
    ] http_request                   response_time_ms=2213.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=11'
    ] http_request                   response_time_ms=1927.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=10'
    ] http_request                   response_time_ms=96.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/undergraduate-academic-scholarships/152222/
    ] http_request                   response_time_ms=12.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-communication-distinction-award/25602/
    ] http_request                   response_time_ms=1916.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=11'
    ] http_request                   response_time_ms=1393.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=11'
    ] http_request                   response_time_ms=13.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-high-achiever-award/121563/
    ] http_request                   response_time_ms=8.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/master-of-applied-engineering-(mappe)-bursary/154183/
    ] http_request                   response_time_ms=2177.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=10'
    ] http_request                   response_time_ms=2057.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=10'
    ] http_request                   response_time_ms=1012.3 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=15'
    ] http_request                   response_time_ms=42.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-english-distinction-award/70793/
    ] http_request                   response_time_ms=2005.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=12'
    ] http_request                   response_time_ms=2032.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=13'
    ] http_request                   response_time_ms=1932.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=14'
    ] http_request                   response_time_ms=296.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/top-achiever-scholarships/110570/
    ] http_request                   response_time_ms=913.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=15'
    ] http_request                   response_time_ms=57.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-for-non-ucd-students-graduates/148208/
    ] http_request                   response_time_ms=8.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/global-excellence-undergraduate-scholarships/129919/
    ] http_request                   response_time_ms=652.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=14'
    ] http_request                   response_time_ms=10.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/school-of-social-work-and-social-policy-international-postgraduate-taught-scholarship/166837/
    ] http_request                   response_time_ms=1231.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=13'
    ] http_request                   response_time_ms=8.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/global-scholarship/166278/
    ] http_request                   response_time_ms=2152.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=11'
    ] http_request                   response_time_ms=9.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/faculty-of-engineering-computing-international-scholarship/161080/
    ] http_request                   response_time_ms=1003.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=15'
    ] http_request                   response_time_ms=53.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=13'
    ] http_request                   response_time_ms=13.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/dr-jonathan-ks-chiu-and-dr-margaret-sau-sheung-ip-undergraduate-scholarship/161386/
    ] http_request                   response_time_ms=2700.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=10'
    ] http_request                   response_time_ms=1949.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=14'
    ] http_request                   response_time_ms=9.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/undergraduate-academic-scholarships/152222/
    ] http_request                   response_time_ms=36.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=13'
    ] http_request                   response_time_ms=2378.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=12'
    ] http_request                   response_time_ms=2405.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=13'
    ] http_request                   response_time_ms=1344.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=14'
    ] http_request                   response_time_ms=1755.5 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=16'
    ] http_request                   response_time_ms=1245.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=15'
    ] http_request                   response_time_ms=583.3 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=school&page=2'
    ] http_request                   response_time_ms=623.3 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=doctorate&page=2'
    ] http_request                   response_time_ms=1856.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=14'
    ] http_request                   response_time_ms=513.6 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=undergraduate&page=2'
    ] http_request                   response_time_ms=904.1 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=17'
    ] http_request                   response_time_ms=2459.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=13'
    ] http_request                   response_time_ms=192.2 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=foundation&page=2'
    ] http_request                   response_time_ms=2344.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=13'
    ] http_request                   response_time_ms=1586.2 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=postgraduate&page=2'
    ] http_request                   response_time_ms=596.6 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=undergraduate&page=2'
    ] http_request                   response_time_ms=905.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=15'
    ] http_request                   response_time_ms=1904.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=15'
    ] http_request                   response_time_ms=521.7 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=postgraduate&page=2'
    ] http_request                   response_time_ms=1974.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=14'
    ] http_request                   response_time_ms=855.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=17'
    ] http_request                   response_time_ms=814.3 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=18'
    ] http_request                   response_time_ms=2362.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=14'
    ] http_request                   response_time_ms=2775.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=15'
    ] http_request                   response_time_ms=920.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/sports-scholarship/164359/
    ] http_request                   response_time_ms=2176.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=14'
    ] http_request                   response_time_ms=1826.0 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=pre-degree-vocational&page=2'
    ] http_request                   response_time_ms=2409.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=15'
    ] http_request                   response_time_ms=2078.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=15'
    ] http_request                   response_time_ms=2281.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=13'
    ] http_request                   response_time_ms=806.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-american-degree-program-distinction-award/25611/
    ] http_request                   response_time_ms=1965.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=14'
    ] http_request                   response_time_ms=959.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=13'
    ] http_request                   response_time_ms=1046.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=15'
    ] http_request                   response_time_ms=2363.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=13'
    ] http_request                   response_time_ms=2186.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=16'
    ] http_request                   response_time_ms=1668.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/early-childhood-education-and-care-(ecec)-scholarship/162598/
    ] http_request                   response_time_ms=1965.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=17'
    ] http_request                   response_time_ms=33.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/graduate-research-pathway-scholarship/154178/
    ] http_request                   response_time_ms=1724.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-management-studies-distinction-award/25662/
    ] http_request                   response_time_ms=22.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/sports-scholarship/164359/
    ] http_request                   response_time_ms=22.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=17'
    ] http_request                   response_time_ms=14.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/early-childhood-education-and-care-(ecec)-scholarship/162598/
    ] http_request                   response_time_ms=11.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-american-degree-program-distinction-award/25611/
    ] http_request                   response_time_ms=10.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-management-studies-distinction-award/25662/
    ] http_request                   response_time_ms=658.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/mitchell-scholarship/167640/
    ] http_request                   response_time_ms=2621.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=16'
    ] http_request                   response_time_ms=3567.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=18'
    ] http_request                   response_time_ms=20.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/graduate-research-pathway-scholarship/154178/
    ] http_request                   response_time_ms=1880.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=18'
    ] http_request                   response_time_ms=2011.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=17'
    ] http_request                   response_time_ms=3730.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=14'
    ] http_request                   response_time_ms=892.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=16'
    ] http_request                   response_time_ms=1871.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=16'
    ] http_request                   response_time_ms=871.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=18'
    ] http_request                   response_time_ms=1806.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=16'
    ] http_request                   response_time_ms=21.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/mitchell-scholarship/167640/
    ] http_request                   response_time_ms=4500.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=16'
    ] http_request                   response_time_ms=1941.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=18'
    ] http_request                   response_time_ms=4868.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=18'
    ] http_request                   response_time_ms=350.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/sports-scholarship/164359/
    ] http_request                   response_time_ms=2089.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=17'
    ] http_request                   response_time_ms=2190.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=16'
    ] http_request                   response_time_ms=1857.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/female-in-engineering-scholarship/154179/
    ] http_request                   response_time_ms=2743.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=18'
    ] http_request                   response_time_ms=1830.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-education-distinction-award/70825/
    ] http_request                   response_time_ms=2845.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=17'
    ] http_request                   response_time_ms=2122.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=18'
    ] http_request                   response_time_ms=4078.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-education-distinction-award/70825/
    ] http_request                   response_time_ms=1802.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/inti-international-university-and-colleges/international-education-scholarship/166891/
    ] http_request                   response_time_ms=334.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/early-childhood-education-and-care-(ecec)-scholarship/162598/
    ] http_request                   response_time_ms=1739.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/high-achiever-scholarships/110571/
    ] http_request                   response_time_ms=4284.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/inti-international-university-and-colleges/international-education-scholarship/166891/
    ] http_request                   response_time_ms=2034.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-pharmacy-excellence-award/128656/
    ] http_request                   response_time_ms=5234.1 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=19'
    ] http_request                   response_time_ms=4109.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/high-achiever-scholarships/110571/
    ] http_request                   response_time_ms=3950.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-pharmacy-excellence-award/128656/
    ] http_request                   response_time_ms=1702.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=16'
    ] http_request                   response_time_ms=4891.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/female-in-engineering-scholarship/154179/
    ] http_request                   response_time_ms=4114.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=18'
    ] http_request                   response_time_ms=820.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-american-degree-program-distinction-award/25611/
    ] http_request                   response_time_ms=2828.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=17'
    ] http_request                   response_time_ms=3898.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/meb-bursary/154182/
    ] http_request                   response_time_ms=323.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-management-studies-distinction-award/25662/
    ] http_request                   response_time_ms=5871.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=17'
    ] http_request                   response_time_ms=2337.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/meb-bursary/154182/
    ] http_request                   response_time_ms=2241.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=17'
    ] http_request                   response_time_ms=5339.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=16'
    ] http_request                   response_time_ms=367.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/female-in-engineering-scholarship/154179/
    ] http_request                   response_time_ms=1547.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=20'
    ] http_request                   response_time_ms=83.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-education-distinction-award/70825/
    ] http_request                   response_time_ms=5218.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=17'
    ] http_request                   response_time_ms=177.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/inti-international-university-and-colleges/international-education-scholarship/166891/
    ] http_request                   response_time_ms=5004.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=16'
    ] http_request                   response_time_ms=171.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/high-achiever-scholarships/110571/
    ] http_request                   response_time_ms=6056.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=18'
    ] http_request                   response_time_ms=282.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-pharmacy-excellence-award/128656/
    ] http_request                   response_time_ms=52.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/graduate-research-pathway-scholarship/154178/
    ] http_request                   response_time_ms=10.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/meb-bursary/154182/
    ] http_request                   response_time_ms=3125.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=18'
    ] http_request                   response_time_ms=1811.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=19'
    ] http_request                   response_time_ms=1131.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=21'
    ] http_request                   response_time_ms=11.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/mitchell-scholarship/167640/
    ] http_request                   response_time_ms=1106.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=19'
    ] http_request                   response_time_ms=11.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/sports-scholarship/164359/
    ] http_request                   response_time_ms=30.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=20'
    ] http_request                   response_time_ms=2686.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=21'
    ] http_request                   response_time_ms=3297.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=19'
    ] http_request                   response_time_ms=131.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/early-childhood-education-and-care-(ecec)-scholarship/162598/
    ] http_request                   response_time_ms=342.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=21'
    ] http_request                   response_time_ms=1424.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=20'
    ] http_request                   response_time_ms=1255.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=21'
    ] http_request                   response_time_ms=185.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-education-distinction-award/70825/
    ] http_request                   response_time_ms=397.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=19'
    ] http_request                   response_time_ms=1049.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=20'
    ] http_request                   response_time_ms=2560.5 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=20'
    ] listing_progress               collected=240 page=20 scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=89.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-american-degree-program-distinction-award/25611/
    ] http_request                   response_time_ms=277.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=20'
    ] http_request                   response_time_ms=2459.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=20'
    ] http_request                   response_time_ms=13.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-management-studies-distinction-award/25662/
    ] http_request                   response_time_ms=1179.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=21'
    ] http_request                   response_time_ms=11.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/female-in-engineering-scholarship/154179/
    ] http_request                   response_time_ms=12.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/inti-international-university-and-colleges/international-education-scholarship/166891/
    ] http_request                   response_time_ms=10.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/high-achiever-scholarships/110571/
    ] http_request                   response_time_ms=11.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-pharmacy-excellence-award/128656/
    ] http_request                   response_time_ms=831.6 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=21'
    ] http_request                   response_time_ms=11.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/graduate-research-pathway-scholarship/154178/
    ] http_request                   response_time_ms=1031.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=19'
    ] http_request                   response_time_ms=11.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/meb-bursary/154182/
    ] http_request                   response_time_ms=11.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/mitchell-scholarship/167640/
    ] http_request                   response_time_ms=1449.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=21'
    ] http_request                   response_time_ms=2179.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=19'
    ] http_request                   response_time_ms=2648.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=19'
    ] http_request                   response_time_ms=879.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=20'
    ] http_request                   response_time_ms=1305.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=20'
    ] http_request                   response_time_ms=791.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=19'
    ] http_request                   response_time_ms=895.8 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=22'
    ] http_request                   response_time_ms=1713.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=20'
    ] http_request                   response_time_ms=279.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/sports-scholarship/164359/
    ] http_request                   response_time_ms=89.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/early-childhood-education-and-care-(ecec)-scholarship/162598/
    ] http_request                   response_time_ms=11.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-american-degree-program-distinction-award/25611/
    ] http_request                   response_time_ms=1955.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=21'
    ] http_request                   response_time_ms=1905.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=19'
    ] http_request                   response_time_ms=132.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-management-studies-distinction-award/25662/
    ] http_request                   response_time_ms=8.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/female-in-engineering-scholarship/154179/
    ] http_request                   response_time_ms=1933.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=21'
    ] http_request                   response_time_ms=1961.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=19'
    ] http_request                   response_time_ms=1112.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=22'
    ] http_request                   response_time_ms=710.8 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=23'
    ] http_request                   response_time_ms=47.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-education-distinction-award/70825/
    ] http_request                   response_time_ms=8.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/inti-international-university-and-colleges/international-education-scholarship/166891/
    ] http_request                   response_time_ms=10.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/high-achiever-scholarships/110571/
    ] http_request                   response_time_ms=1103.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=24'
    ] http_request                   response_time_ms=9.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-pharmacy-excellence-award/128656/
    ] http_request                   response_time_ms=2104.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=20'
    ] http_request                   response_time_ms=2306.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=21'
    ] http_request                   response_time_ms=2003.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=21'
    ] http_request                   response_time_ms=794.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=22'
    ] http_request                   response_time_ms=296.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/graduate-research-pathway-scholarship/154178/
    ] http_request                   response_time_ms=958.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=23'
    ] http_request                   response_time_ms=38.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/meb-bursary/154182/
    ] http_request                   response_time_ms=32.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=24'
    ] http_request                   response_time_ms=9.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/mitchell-scholarship/167640/
    ] http_request                   response_time_ms=860.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=23'
    ] http_request                   response_time_ms=10.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/sports-scholarship/164359/
    ] http_request                   response_time_ms=10.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/early-childhood-education-and-care-(ecec)-scholarship/162598/
    ] http_request                   response_time_ms=9.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-american-degree-program-distinction-award/25611/
    ] http_request                   response_time_ms=1974.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=23'
    ] http_request                   response_time_ms=9.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-management-studies-distinction-award/25662/
    ] http_request                   response_time_ms=2277.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=22'
    ] http_request                   response_time_ms=2076.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=24'
    ] http_request                   response_time_ms=2147.3 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=24'
    ] http_request                   response_time_ms=2091.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=24'
    ] http_request                   response_time_ms=3046.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=23'
    ] http_request                   response_time_ms=297.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/female-in-engineering-scholarship/154179/
    ] http_request                   response_time_ms=50.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-education-distinction-award/70825/
    ] http_request                   response_time_ms=1467.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=22'
    ] http_request                   response_time_ms=2484.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=22'
    ] http_request                   response_time_ms=49.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/inti-international-university-and-colleges/international-education-scholarship/166891/
    ] http_request                   response_time_ms=2391.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=24'
    ] http_request                   response_time_ms=293.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/high-achiever-scholarships/110571/
    ] http_request                   response_time_ms=2132.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=23'
    ] http_request                   response_time_ms=1321.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=22'
    ] http_request                   response_time_ms=1525.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=23'
    ] http_request                   response_time_ms=54.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-pharmacy-excellence-award/128656/
    ] http_request                   response_time_ms=2570.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=22'
    ] http_request                   response_time_ms=1969.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=23'
    ] http_request                   response_time_ms=1043.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=23'
    ] http_request                   response_time_ms=2049.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=24'
    ] http_request                   response_time_ms=132.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/graduate-research-pathway-scholarship/154178/
    ] http_request                   response_time_ms=8.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/meb-bursary/154182/
    ] http_request                   response_time_ms=10.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/mitchell-scholarship/167640/
    ] http_request                   response_time_ms=1434.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=24'
    ] http_request                   response_time_ms=124.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/sports-scholarship/164359/
    ] http_request                   response_time_ms=1583.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=22'
    ] http_request                   response_time_ms=2550.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=24'
    ] http_request                   response_time_ms=11.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/early-childhood-education-and-care-(ecec)-scholarship/162598/
    ] http_request                   response_time_ms=52.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=26'
    ] http_request                   response_time_ms=2838.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=22'
    ] http_request                   response_time_ms=2244.8 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=25'
    ] http_request                   response_time_ms=832.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=25'
    ] http_request                   response_time_ms=52.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-american-degree-program-distinction-award/25611/
    ] http_request                   response_time_ms=1840.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=23'
    ] http_request                   response_time_ms=9.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-management-studies-distinction-award/25662/
    ] http_request                   response_time_ms=958.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=26'
    ] http_request                   response_time_ms=9.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/female-in-engineering-scholarship/154179/
    ] http_request                   response_time_ms=55.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=27'
    ] http_request                   response_time_ms=9.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-education-distinction-award/70825/
    ] http_request                   response_time_ms=1960.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=24'
    ] http_request                   response_time_ms=1122.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=25'
    ] http_request                   response_time_ms=10.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/inti-international-university-and-colleges/international-education-scholarship/166891/
    ] http_request                   response_time_ms=8.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/high-achiever-scholarships/110571/
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-pharmacy-excellence-award/128656/
    ] http_request                   response_time_ms=53.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=26'
    ] http_request                   response_time_ms=1689.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=27'
    ] http_request                   response_time_ms=868.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=25'
    ] http_request                   response_time_ms=10.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/graduate-research-pathway-scholarship/154178/
    ] http_request                   response_time_ms=893.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=26'
    ] http_request                   response_time_ms=1365.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=25'
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/meb-bursary/154182/
    ] http_request                   response_time_ms=9.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/mitchell-scholarship/167640/
    ] http_request                   response_time_ms=3027.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=22'
    ] http_request                   response_time_ms=10.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/sports-scholarship/164359/
    ] http_request                   response_time_ms=2790.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=24'
    ] http_request                   response_time_ms=2938.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=23'
    ] http_request                   response_time_ms=10.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/early-childhood-education-and-care-(ecec)-scholarship/162598/
    ] http_request                   response_time_ms=812.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=25'
    ] http_request                   response_time_ms=1944.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=26'
    ] http_request                   response_time_ms=882.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=27'
    ] http_request                   response_time_ms=2344.8 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=26'
    ] http_request                   response_time_ms=40.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-american-degree-program-distinction-award/25611/
    ] http_request                   response_time_ms=8.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-management-studies-distinction-award/25662/
    ] http_request                   response_time_ms=2589.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=27'
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/female-in-engineering-scholarship/154179/
    ] http_request                   response_time_ms=2022.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=25'
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-education-distinction-award/70825/
    ] http_request                   response_time_ms=579.3 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=27'
    ] http_request                   response_time_ms=10.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/inti-international-university-and-colleges/international-education-scholarship/166891/
    ] http_request                   response_time_ms=8.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-southampton-malaysia/high-achiever-scholarships/110571/
    ] http_request                   response_time_ms=2550.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=27'
    ] http_request                   response_time_ms=2298.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=27'
    ] http_request                   response_time_ms=1310.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=26'
    ] http_request                   response_time_ms=703.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=27'
    ] http_request                   response_time_ms=262.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/monash-pharmacy-excellence-award/128656/
    ] http_request                   response_time_ms=2070.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=25'
    ] http_request                   response_time_ms=682.5 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=28'
    ] http_request                   response_time_ms=2102.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=26'
    ] http_request                   response_time_ms=990.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=28'
    ] http_request                   response_time_ms=2410.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=26'
    ] http_request                   response_time_ms=1030.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=29'
    ] http_request                   response_time_ms=908.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=30'
    ] http_request                   response_time_ms=134.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/meb-bursary/154182/
    ] http_request                   response_time_ms=488.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/monash-university-malaysia/graduate-research-pathway-scholarship/154178/
    ] http_request                   response_time_ms=2325.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=27'
    ] http_request                   response_time_ms=333.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/mitchell-scholarship/167640/
    ] http_request                   response_time_ms=2109.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=27'
    ] http_request                   response_time_ms=2492.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=25'
    ] http_request                   response_time_ms=903.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=29'
    ] http_request                   response_time_ms=2228.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=25'
    ] http_request                   response_time_ms=521.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=29'
    ] http_request                   response_time_ms=2375.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=26'
    ] http_request                   response_time_ms=1663.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=28'
    ] http_request                   response_time_ms=1958.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=27'
    ] http_request                   response_time_ms=948.5 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=school&page=3'
    ] http_request                   response_time_ms=579.5 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=undergraduate&page=3'
    ] http_request                   response_time_ms=660.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=30'
    ] http_request                   response_time_ms=911.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=28'
    ] http_request                   response_time_ms=1181.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=30'
    ] http_request                   response_time_ms=2553.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=25'
    ] http_request                   response_time_ms=1952.8 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=29'
    ] http_request                   response_time_ms=2048.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=30'
    ] http_request                   response_time_ms=798.4 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=undergraduate&page=3'
    ] http_request                   response_time_ms=67.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-excellence-merit-based-scholarship/166283/
    ] http_request                   response_time_ms=959.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=28'
    ] http_request                   response_time_ms=1690.3 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=doctorate&page=3'
    ] http_request                   response_time_ms=43.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/ucd-global-excellence-scholarships/139058/
    ] http_request                   response_time_ms=826.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=30'
    ] http_request                   response_time_ms=3421.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=26'
    ] http_request                   response_time_ms=2720.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=28'
    ] http_request                   response_time_ms=957.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=31'
    ] http_request                   response_time_ms=1714.0 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=foundation&page=3'
    ] http_request                   response_time_ms=1724.0 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=postgraduate&page=3'
    ] http_request                   response_time_ms=1817.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=29'
    ] http_request                   response_time_ms=78.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/faculty-of-science-and-engineering-scholarships/149485/
    ] http_request                   response_time_ms=2368.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=29'
    ] http_request                   response_time_ms=1871.9 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=postgraduate&page=3'
    ] http_request                   response_time_ms=1099.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=28'
    ] http_request                   response_time_ms=2412.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=28'
    ] http_request                   response_time_ms=1797.6 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=30'
    ] http_request                   response_time_ms=2252.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=30'
    ] http_request                   response_time_ms=941.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=30'
    ] http_request                   response_time_ms=1767.6 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=pre-degree-vocational&page=3'
    ] listing_progress               collected=360 page=30 scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=2010.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=29'
    ] http_request                   response_time_ms=1705.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/masters-academic-merit-scholarships/152220/
    ] http_request                   response_time_ms=1034.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=28'
    ] http_request                   response_time_ms=843.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-region-based-(china)-claddagh-scholarship/164318/
    ] http_request                   response_time_ms=1193.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-region-based-(usa)-idea-scholarship/164352/
    ] http_request                   response_time_ms=247.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-marketing-and-retail-innovation-scholarships/139066/
    ] http_request                   response_time_ms=111.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=30'
    ] http_request                   response_time_ms=2331.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=32'
    ] http_request                   response_time_ms=22.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/homecoming-scholarship/166291/
    ] http_request                   response_time_ms=1552.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=29'
    ] http_request                   response_time_ms=2280.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=33'
    ] http_request                   response_time_ms=1967.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/postgraduate-e3-balanced-solutions-for-a-better-world-scholarship/139049/
    ] http_request                   response_time_ms=170.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/masters-academic-merit-scholarships/152220/
    ] http_request                   response_time_ms=49.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-excellence-merit-based-scholarship/166283/
    ] http_request                   response_time_ms=10.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/ucd-global-excellence-scholarships/139058/
    ] http_request                   response_time_ms=2444.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=29'
    ] http_request                   response_time_ms=934.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/merit-based-academic-scholarship-(postgraduate)/166287/
    ] http_request                   response_time_ms=2037.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=30'
    ] http_request                   response_time_ms=340.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/postgraduate-e3-balanced-solutions-for-a-better-world-scholarship/139049/
    ] http_request                   response_time_ms=1123.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=33'
    ] http_request                   response_time_ms=1677.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=29'
    ] http_request                   response_time_ms=52.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-region-based-(usa)-idea-scholarship/164352/
    ] http_request                   response_time_ms=11.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/faculty-of-science-and-engineering-scholarships/149485/
    ] http_request                   response_time_ms=1671.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/brazilian-student-ambassador-scholarships/166275/
    ] http_request                   response_time_ms=2254.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-(including-shannon-college-of-hotel-management)-undergraduate-merit-awards/164350/
    ] http_request                   response_time_ms=1964.0 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=31'
    ] http_request                   response_time_ms=13.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-region-based-(china)-claddagh-scholarship/164318/
    ] http_request                   response_time_ms=58.9 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=32'
    ] http_request                   response_time_ms=12.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-(including-shannon-college-of-hotel-management)-undergraduate-merit-awards/164350/
    ] http_request                   response_time_ms=11.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-marketing-and-retail-innovation-scholarships/139066/
    ] http_request                   response_time_ms=44.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=31'
    ] http_request                   response_time_ms=2838.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=28'
    ] http_request                   response_time_ms=102.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/brazilian-student-ambassador-scholarships/166275/
    ] http_request                   response_time_ms=2246.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=31'
    ] http_request                   response_time_ms=918.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=33'
    ] http_request                   response_time_ms=2035.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=28'
    ] http_request                   response_time_ms=11.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/merit-based-academic-scholarship-(postgraduate)/166287/
    ] http_request                   response_time_ms=2038.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=29'
    ] http_request                   response_time_ms=1937.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=30'
    ] http_request                   response_time_ms=126.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/homecoming-scholarship/166291/
    ] http_request                   response_time_ms=11.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/masters-academic-merit-scholarships/152220/
    ] http_request                   response_time_ms=2752.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=32'
    ] http_request                   response_time_ms=11.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-excellence-merit-based-scholarship/166283/
    ] http_request                   response_time_ms=11.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/ucd-global-excellence-scholarships/139058/
    ] http_request                   response_time_ms=2426.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=31'
    ] http_request                   response_time_ms=2292.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=32'
    ] http_request                   response_time_ms=2072.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=31'
    ] http_request                   response_time_ms=1969.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=32'
    ] http_request                   response_time_ms=1605.9 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=33'
    ] http_request                   response_time_ms=94.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/postgraduate-e3-balanced-solutions-for-a-better-world-scholarship/139049/
    ] http_request                   response_time_ms=1901.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=33'
    ] http_request                   response_time_ms=1627.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=32'
    ] http_request                   response_time_ms=17.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-region-based-(usa)-idea-scholarship/164352/
    ] http_request                   response_time_ms=2069.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=33'
    ] http_request                   response_time_ms=2170.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=32'
    ] http_request                   response_time_ms=2277.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=31'
    ] http_request                   response_time_ms=148.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/faculty-of-science-and-engineering-scholarships/149485/
    ] http_request                   response_time_ms=14.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-region-based-(china)-claddagh-scholarship/164318/
    ] http_request                   response_time_ms=11.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-(including-shannon-college-of-hotel-management)-undergraduate-merit-awards/164350/
    ] http_request                   response_time_ms=2011.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=34'
    ] http_request                   response_time_ms=2232.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=33'
    ] http_request                   response_time_ms=120.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-marketing-and-retail-innovation-scholarships/139066/
    ] http_request                   response_time_ms=2170.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=35'
    ] http_request                   response_time_ms=1903.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=31'
    ] http_request                   response_time_ms=14.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/brazilian-student-ambassador-scholarships/166275/
    ] http_request                   response_time_ms=1486.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=31'
    ] http_request                   response_time_ms=2136.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=36'
    ] http_request                   response_time_ms=12.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/merit-based-academic-scholarship-(postgraduate)/166287/
    ] http_request                   response_time_ms=854.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=32'
    ] http_request                   response_time_ms=11.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/homecoming-scholarship/166291/
    ] http_request                   response_time_ms=2261.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=32'
    ] http_request                   response_time_ms=12.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/masters-academic-merit-scholarships/152220/
    ] http_request                   response_time_ms=1964.0 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=34'
    ] http_request                   response_time_ms=9.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-excellence-merit-based-scholarship/166283/
    ] http_request                   response_time_ms=80.8 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=35'
    ] http_request                   response_time_ms=8.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/ucd-global-excellence-scholarships/139058/
    ] http_request                   response_time_ms=788.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=34'
    ] http_request                   response_time_ms=2683.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=33'
    ] http_request                   response_time_ms=2047.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=33'
    ] http_request                   response_time_ms=1000.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=35'
    ] http_request                   response_time_ms=13.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/postgraduate-e3-balanced-solutions-for-a-better-world-scholarship/139049/
    ] http_request                   response_time_ms=2297.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=32'
    ] http_request                   response_time_ms=1880.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=33'
    ] http_request                   response_time_ms=10.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-region-based-(usa)-idea-scholarship/164352/
    ] http_request                   response_time_ms=2134.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=31'
    ] http_request                   response_time_ms=2003.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=31'
    ] http_request                   response_time_ms=1307.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=36'
    ] http_request                   response_time_ms=988.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=36'
    ] http_request                   response_time_ms=885.1 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=36'
    ] http_request                   response_time_ms=131.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/faculty-of-science-and-engineering-scholarships/149485/
    ] http_request                   response_time_ms=9.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-region-based-(china)-claddagh-scholarship/164318/
    ] http_request                   response_time_ms=136.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=36'
    ] http_request                   response_time_ms=2079.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=32'
    ] http_request                   response_time_ms=12.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-(including-shannon-college-of-hotel-management)-undergraduate-merit-awards/164350/
    ] http_request                   response_time_ms=173.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=35'
    ] http_request                   response_time_ms=10.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-marketing-and-retail-innovation-scholarships/139066/
    ] http_request                   response_time_ms=1864.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=34'
    ] http_request                   response_time_ms=9.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/brazilian-student-ambassador-scholarships/166275/
    ] http_request                   response_time_ms=2441.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=33'
    ] http_request                   response_time_ms=10.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/merit-based-academic-scholarship-(postgraduate)/166287/
    ] http_request                   response_time_ms=2124.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=35'
    ] http_request                   response_time_ms=975.7 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=37'
    ] http_request                   response_time_ms=42.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/homecoming-scholarship/166291/
    ] http_request                   response_time_ms=1984.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=35'
    ] http_request                   response_time_ms=8.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/masters-academic-merit-scholarships/152220/
    ] http_request                   response_time_ms=819.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=36'
    ] http_request                   response_time_ms=2267.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=34'
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-excellence-merit-based-scholarship/166283/
    ] http_request                   response_time_ms=103.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=34'
    ] http_request                   response_time_ms=1957.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=36'
    ] http_request                   response_time_ms=1060.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=38'
    ] http_request                   response_time_ms=2024.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=34'
    ] http_request                   response_time_ms=1537.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=34'
    ] http_request                   response_time_ms=122.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/ucd-global-excellence-scholarships/139058/
    ] http_request                   response_time_ms=9.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/postgraduate-e3-balanced-solutions-for-a-better-world-scholarship/139049/
    ] http_request                   response_time_ms=9.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-region-based-(usa)-idea-scholarship/164352/
    ] http_request                   response_time_ms=935.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=35'
    ] http_request                   response_time_ms=1004.6 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=38'
    ] http_request                   response_time_ms=30.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=37'
    ] http_request                   response_time_ms=8.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/faculty-of-science-and-engineering-scholarships/149485/
    ] http_request                   response_time_ms=2369.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=35'
    ] http_request                   response_time_ms=10.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-region-based-(china)-claddagh-scholarship/164318/
    ] http_request                   response_time_ms=10.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-(including-shannon-college-of-hotel-management)-undergraduate-merit-awards/164350/
    ] http_request                   response_time_ms=900.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=34'
    ] http_request                   response_time_ms=2260.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=37'
    ] http_request                   response_time_ms=675.1 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=39'
    ] http_request                   response_time_ms=1973.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=39'
    ] http_request                   response_time_ms=168.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-marketing-and-retail-innovation-scholarships/139066/
    ] http_request                   response_time_ms=1969.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=34'
    ] http_request                   response_time_ms=632.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=39'
    ] http_request                   response_time_ms=66.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/brazilian-student-ambassador-scholarships/166275/
    ] http_request                   response_time_ms=850.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=38'
    ] http_request                   response_time_ms=2051.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=36'
    ] http_request                   response_time_ms=1377.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=35'
    ] http_request                   response_time_ms=130.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/merit-based-academic-scholarship-(postgraduate)/166287/
    ] http_request                   response_time_ms=9.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/homecoming-scholarship/166291/
    ] http_request                   response_time_ms=852.0 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=40'
    ] http_request                   response_time_ms=968.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=36'
    ] listing_progress               collected=480 page=40 scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=891.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=37'
    ] http_request                   response_time_ms=770.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=38'
    ] http_request                   response_time_ms=47.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/masters-academic-merit-scholarships/152220/
    ] http_request                   response_time_ms=2136.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=36'
    ] http_request                   response_time_ms=1342.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=34'
    ] http_request                   response_time_ms=10.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-excellence-merit-based-scholarship/166283/
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/ucd-global-excellence-scholarships/139058/
    ] http_request                   response_time_ms=9.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/postgraduate-e3-balanced-solutions-for-a-better-world-scholarship/139049/
    ] http_request                   response_time_ms=2741.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=35'
    ] http_request                   response_time_ms=897.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=38'
    ] http_request                   response_time_ms=10.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-region-based-(usa)-idea-scholarship/164352/
    ] http_request                   response_time_ms=2388.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=36'
    ] http_request                   response_time_ms=804.6 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=41'
    ] http_request                   response_time_ms=1916.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=35'
    ] http_request                   response_time_ms=41.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/faculty-of-science-and-engineering-scholarships/149485/
    ] http_request                   response_time_ms=10.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-region-based-(china)-claddagh-scholarship/164318/
    ] http_request                   response_time_ms=8.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-(including-shannon-college-of-hotel-management)-undergraduate-merit-awards/164350/
    ] http_request                   response_time_ms=1119.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=39'
    ] http_request                   response_time_ms=10.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-marketing-and-retail-innovation-scholarships/139066/
    ] http_request                   response_time_ms=8.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/brazilian-student-ambassador-scholarships/166275/
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/merit-based-academic-scholarship-(postgraduate)/166287/
    ] http_request                   response_time_ms=704.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=40'
    ] http_request                   response_time_ms=1028.6 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=42'
    ] http_request                   response_time_ms=11.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/homecoming-scholarship/166291/
    ] http_request                   response_time_ms=2578.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=39'
    ] http_request                   response_time_ms=57.7 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=43'
    ] http_request                   response_time_ms=10.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/masters-academic-merit-scholarships/152220/
    ] http_request                   response_time_ms=803.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=41'
    ] http_request                   response_time_ms=2773.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=37'
    ] http_request                   response_time_ms=1929.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=37'
    ] http_request                   response_time_ms=12.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-excellence-merit-based-scholarship/166283/
    ] http_request                   response_time_ms=8.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/ucd-global-excellence-scholarships/139058/
    ] http_request                   response_time_ms=9.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/postgraduate-e3-balanced-solutions-for-a-better-world-scholarship/139049/
    ] http_request                   response_time_ms=2675.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=37'
    ] http_request                   response_time_ms=9.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-region-based-(usa)-idea-scholarship/164352/
    ] http_request                   response_time_ms=2250.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=38'
    ] http_request                   response_time_ms=2925.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=39'
    ] http_request                   response_time_ms=2807.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=38'
    ] http_request                   response_time_ms=678.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=37'
    ] http_request                   response_time_ms=167.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/faculty-of-science-and-engineering-scholarships/149485/
    ] http_request                   response_time_ms=1311.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=38'
    ] http_request                   response_time_ms=745.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=38'
    ] http_request                   response_time_ms=1549.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=42'
    ] http_request                   response_time_ms=1953.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=41'
    ] http_request                   response_time_ms=2380.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=39'
    ] http_request                   response_time_ms=388.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-region-based-(china)-claddagh-scholarship/164318/
    ] http_request                   response_time_ms=2236.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=42'
    ] http_request                   response_time_ms=556.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=37'
    ] http_request                   response_time_ms=2137.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=40'
    ] http_request                   response_time_ms=291.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-(including-shannon-college-of-hotel-management)-undergraduate-merit-awards/164350/
    ] http_request                   response_time_ms=1310.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=37'
    ] http_request                   response_time_ms=2215.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=37'
    ] http_request                   response_time_ms=1830.8 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=44'
    ] http_request                   response_time_ms=134.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-marketing-and-retail-innovation-scholarships/139066/
    ] http_request                   response_time_ms=1872.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=39'
    ] http_request                   response_time_ms=131.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/brazilian-student-ambassador-scholarships/166275/
    ] http_request                   response_time_ms=11.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/merit-based-academic-scholarship-(postgraduate)/166287/
    ] http_request                   response_time_ms=1300.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=38'
    ] http_request                   response_time_ms=9.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/homecoming-scholarship/166291/
    ] http_request                   response_time_ms=10.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/national-college-of-ireland/masters-academic-merit-scholarships/152220/
    ] http_request                   response_time_ms=724.6 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=45'
    ] http_request                   response_time_ms=8.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-excellence-merit-based-scholarship/166283/
    ] http_request                   response_time_ms=2297.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=39'
    ] http_request                   response_time_ms=2270.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=38'
    ] http_request                   response_time_ms=56.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/ucd-global-excellence-scholarships/139058/
    ] http_request                   response_time_ms=1065.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=41'
    ] http_request                   response_time_ms=2219.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=39'
    ] http_request                   response_time_ms=1619.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=39'
    ] http_request                   response_time_ms=253.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/postgraduate-e3-balanced-solutions-for-a-better-world-scholarship/139049/
    ] http_request                   response_time_ms=46.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-region-based-(usa)-idea-scholarship/164352/
    ] http_request                   response_time_ms=9.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/faculty-of-science-and-engineering-scholarships/149485/
    ] http_request                   response_time_ms=10.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-region-based-(china)-claddagh-scholarship/164318/
    ] http_request                   response_time_ms=1991.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=40'
    ] http_request                   response_time_ms=1520.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=40'
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-and-law-(including-shannon-college-of-hotel-management)-undergraduate-merit-awards/164350/
    ] http_request                   response_time_ms=11.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-marketing-and-retail-innovation-scholarships/139066/
    ] http_request                   response_time_ms=1463.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=40'
    ] http_request                   response_time_ms=661.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=41'
    ] http_request                   response_time_ms=1986.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=42'
    ] http_request                   response_time_ms=10.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/brazilian-student-ambassador-scholarships/166275/
    ] http_request                   response_time_ms=1194.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=40'
    ] http_request                   response_time_ms=1626.1 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=46'
    ] http_request                   response_time_ms=1892.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=42'
    ] http_request                   response_time_ms=2031.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=41'
    ] http_request                   response_time_ms=289.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/merit-based-academic-scholarship-(postgraduate)/166287/
    ] http_request                   response_time_ms=2002.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=41'
    ] http_request                   response_time_ms=48.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/homecoming-scholarship/166291/
    ] http_request                   response_time_ms=1839.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=42'
    ] http_request                   response_time_ms=692.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=40'
    ] http_request                   response_time_ms=1019.3 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=47'
    ] http_request                   response_time_ms=2148.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=42'
    ] http_request                   response_time_ms=29.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=42'
    ] http_request                   response_time_ms=1747.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=45'
    ] http_request                   response_time_ms=1592.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=41'
    ] http_request                   response_time_ms=511.5 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=48'
    ] http_request                   response_time_ms=602.0 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=foundation&page=4'
    ] http_request                   response_time_ms=2533.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=43'
    ] http_request                   response_time_ms=1509.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=42'
    ] http_request                   response_time_ms=2571.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=44'
    ] http_request                   response_time_ms=2637.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=44'
    ] http_request                   response_time_ms=870.8 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=postgraduate&page=4'
    ] http_request                   response_time_ms=1716.3 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=school&page=4'
    ] http_request                   response_time_ms=2841.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=45'
    ] http_request                   response_time_ms=1697.0 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=undergraduate&page=4'
    ] http_request                   response_time_ms=2871.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=43'
    ] http_request                   response_time_ms=1127.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=41'
    ] http_request                   response_time_ms=840.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=45'
    ] http_request                   response_time_ms=1050.5 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=postgraduate&page=4'
    ] http_request                   response_time_ms=2052.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=40'
    ] http_request                   response_time_ms=1750.1 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=undergraduate&page=4'
    ] http_request                   response_time_ms=1163.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=44'
    ] http_request                   response_time_ms=2153.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=41'
    ] http_request                   response_time_ms=2105.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=42'
    ] http_request                   response_time_ms=1853.4 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=doctorate&page=4'
    ] http_request                   response_time_ms=293.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/regional-excellence-scholarships/167682/
    ] http_request                   response_time_ms=2165.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=42'
    ] http_request                   response_time_ms=2071.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=40'
    ] http_request                   response_time_ms=976.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-open-to-vietnamese-students/139070/
    ] http_request                   response_time_ms=1757.2 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=49'
    ] http_request                   response_time_ms=2002.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=43'
    ] http_request                   response_time_ms=91.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-undergraduate-merit-awards/161100/
    ] http_request                   response_time_ms=2651.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=40'
    ] http_request                   response_time_ms=2714.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=41'
    ] http_request                   response_time_ms=1916.8 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=pre-degree-vocational&page=4'
    ] http_request                   response_time_ms=1449.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=45'
    ] http_request                   response_time_ms=46.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-merit-scholarships/161082/
    ] http_request                   response_time_ms=708.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/professor-brian-fynes-memorial-scholarship/148211/
    ] http_request                   response_time_ms=18.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=46'
    ] http_request                   response_time_ms=1063.9 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=50'
    ] listing_progress               collected=600 page=50 scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=2653.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=43'
    ] http_request                   response_time_ms=47.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/tus-global-scholarship-(previously-presidents-scholarship)/166289/
    ] http_request                   response_time_ms=22.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-humanities-and-social-sciences-bursary/161081/
    ] http_request                   response_time_ms=2502.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=44'
    ] http_request                   response_time_ms=2007.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/ul-family-alumni-scholarship/167749/
    ] http_request                   response_time_ms=11.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-open-to-vietnamese-students/139070/
    ] http_request                   response_time_ms=1742.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-postgraduate-taught-awards/164315/
    ] http_request                   response_time_ms=626.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=45'
    ] http_request                   response_time_ms=10.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/regional-excellence-scholarships/167682/
    ] http_request                   response_time_ms=10.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/ul-family-alumni-scholarship/167749/
    ] http_request                   response_time_ms=1199.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=44'
    ] http_request                   response_time_ms=11.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-postgraduate-taught-awards/164315/
    ] http_request                   response_time_ms=2638.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=43'
    ] http_request                   response_time_ms=10.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-undergraduate-merit-awards/161100/
    ] http_request                   response_time_ms=2057.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=43'
    ] http_request                   response_time_ms=13.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/professor-brian-fynes-memorial-scholarship/148211/
    ] http_request                   response_time_ms=1218.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=48'
    ] http_request                   response_time_ms=2159.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=44'
    ] http_request                   response_time_ms=2007.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/msc-law-and-finance-scholarship/166271/
    ] http_request                   response_time_ms=2749.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=44'
    ] http_request                   response_time_ms=2580.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=45'
    ] http_request                   response_time_ms=2234.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-international-undergraduate-scholarships/166280/
    ] http_request                   response_time_ms=203.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-international-undergraduate-scholarships/166280/
    ] http_request                   response_time_ms=2351.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=45'
    ] http_request                   response_time_ms=1729.0 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=51'
    ] http_request                   response_time_ms=2048.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-arts-celtic-studies-and-social-sciences-international-undergraduate-scholarships/166282/
    ] http_request                   response_time_ms=771.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=44'
    ] http_request                   response_time_ms=1073.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=44'
    ] http_request                   response_time_ms=1132.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=45'
    ] http_request                   response_time_ms=2534.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=43'
    ] http_request                   response_time_ms=1971.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=47'
    ] http_request                   response_time_ms=331.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/msc-law-and-finance-scholarship/166271/
    ] http_request                   response_time_ms=2160.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=46'
    ] http_request                   response_time_ms=2062.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=47'
    ] http_request                   response_time_ms=1356.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=45'
    ] http_request                   response_time_ms=481.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-merit-scholarships/161082/
    ] http_request                   response_time_ms=54.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-arts-celtic-studies-and-social-sciences-international-undergraduate-scholarships/166282/
    ] http_request                   response_time_ms=1608.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=43'
    ] http_request                   response_time_ms=868.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=48'
    ] http_request                   response_time_ms=10.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/tus-global-scholarship-(previously-presidents-scholarship)/166289/
    ] http_request                   response_time_ms=10.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-humanities-and-social-sciences-bursary/161081/
    ] http_request                   response_time_ms=12.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-open-to-vietnamese-students/139070/
    ] http_request                   response_time_ms=2544.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=48'
    ] http_request                   response_time_ms=57.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=48'
    ] http_request                   response_time_ms=2705.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=43'
    ] http_request                   response_time_ms=853.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=44'
    ] http_request                   response_time_ms=128.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/regional-excellence-scholarships/167682/
    ] http_request                   response_time_ms=11.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/ul-family-alumni-scholarship/167749/
    ] http_request                   response_time_ms=2260.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=46'
    ] http_request                   response_time_ms=13.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-postgraduate-taught-awards/164315/
    ] http_request                   response_time_ms=12.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-undergraduate-merit-awards/161100/
    ] http_request                   response_time_ms=11.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/professor-brian-fynes-memorial-scholarship/148211/
    ] http_request                   response_time_ms=11.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-international-undergraduate-scholarships/166280/
    ] http_request                   response_time_ms=833.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=46'
    ] http_request                   response_time_ms=11.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/msc-law-and-finance-scholarship/166271/
    ] http_request                   response_time_ms=2572.5 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=52'
    ] http_request                   response_time_ms=10.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-merit-scholarships/161082/
    ] http_request                   response_time_ms=2920.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=47'
    ] http_request                   response_time_ms=1140.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=47'
    ] http_request                   response_time_ms=1890.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=45'
    ] http_request                   response_time_ms=996.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=48'
    ] http_request                   response_time_ms=1945.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=47'
    ] http_request                   response_time_ms=262.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-arts-celtic-studies-and-social-sciences-international-undergraduate-scholarships/166282/
    ] http_request                   response_time_ms=49.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/tus-global-scholarship-(previously-presidents-scholarship)/166289/
    ] http_request                   response_time_ms=933.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=47'
    ] http_request                   response_time_ms=3034.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=43'
    ] http_request                   response_time_ms=12.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-humanities-and-social-sciences-bursary/161081/
    ] http_request                   response_time_ms=2419.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=46'
    ] http_request                   response_time_ms=1032.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=50'
    ] http_request                   response_time_ms=15.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-open-to-vietnamese-students/139070/
    ] http_request                   response_time_ms=1921.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=48'
    ] http_request                   response_time_ms=11.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/regional-excellence-scholarships/167682/
    ] http_request                   response_time_ms=2125.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=46'
    ] http_request                   response_time_ms=1879.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=46'
    ] http_request                   response_time_ms=716.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=48'
    ] http_request                   response_time_ms=8.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/ul-family-alumni-scholarship/167749/
    ] http_request                   response_time_ms=2172.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=47'
    ] http_request                   response_time_ms=1899.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=48'
    ] http_request                   response_time_ms=127.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-postgraduate-taught-awards/164315/
    ] http_request                   response_time_ms=1926.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=49'
    ] http_request                   response_time_ms=1744.9 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=53'
    ] http_request                   response_time_ms=922.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=50'
    ] http_request                   response_time_ms=13.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-undergraduate-merit-awards/161100/
    ] http_request                   response_time_ms=1938.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=51'
    ] http_request                   response_time_ms=1765.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=47'
    ] http_request                   response_time_ms=13.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/professor-brian-fynes-memorial-scholarship/148211/
    ] http_request                   response_time_ms=9.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-international-undergraduate-scholarships/166280/
    ] http_request                   response_time_ms=9.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/msc-law-and-finance-scholarship/166271/
    ] http_request                   response_time_ms=11.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-merit-scholarships/161082/
    ] http_request                   response_time_ms=2147.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=49'
    ] http_request                   response_time_ms=1586.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=46'
    ] http_request                   response_time_ms=2578.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=46'
    ] http_request                   response_time_ms=131.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-arts-celtic-studies-and-social-sciences-international-undergraduate-scholarships/166282/
    ] http_request                   response_time_ms=1238.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=49'
    ] http_request                   response_time_ms=11.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/tus-global-scholarship-(previously-presidents-scholarship)/166289/
    ] http_request                   response_time_ms=1928.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=51'
    ] http_request                   response_time_ms=11.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-humanities-and-social-sciences-bursary/161081/
    ] http_request                   response_time_ms=177.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=50'
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-open-to-vietnamese-students/139070/
    ] http_request                   response_time_ms=856.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=49'
    ] http_request                   response_time_ms=1749.0 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=54'
    ] http_request                   response_time_ms=1228.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=47'
    ] http_request                   response_time_ms=10.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/regional-excellence-scholarships/167682/
    ] http_request                   response_time_ms=2162.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=48'
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/ul-family-alumni-scholarship/167749/
    ] http_request                   response_time_ms=2350.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=47'
    ] http_request                   response_time_ms=760.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=51'
    ] http_request                   response_time_ms=11.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-postgraduate-taught-awards/164315/
    ] http_request                   response_time_ms=1327.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=50'
    ] http_request                   response_time_ms=10.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-undergraduate-merit-awards/161100/
    ] http_request                   response_time_ms=2261.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=50'
    ] http_request                   response_time_ms=862.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=49'
    ] http_request                   response_time_ms=1882.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=46'
    ] http_request                   response_time_ms=12.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/professor-brian-fynes-memorial-scholarship/148211/
    ] http_request                   response_time_ms=92.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=54'
    ] http_request                   response_time_ms=2256.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=51'
    ] http_request                   response_time_ms=174.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-international-undergraduate-scholarships/166280/
    ] http_request                   response_time_ms=2130.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=48'
    ] http_request                   response_time_ms=286.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/msc-law-and-finance-scholarship/166271/
    ] http_request                   response_time_ms=1925.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=49'
    ] http_request                   response_time_ms=2056.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=51'
    ] http_request                   response_time_ms=169.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-merit-scholarships/161082/
    ] http_request                   response_time_ms=1067.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=53'
    ] http_request                   response_time_ms=1628.9 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=55'
    ] http_request                   response_time_ms=88.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-arts-celtic-studies-and-social-sciences-international-undergraduate-scholarships/166282/
    ] http_request                   response_time_ms=8.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/tus-global-scholarship-(previously-presidents-scholarship)/166289/
    ] http_request                   response_time_ms=9.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-humanities-and-social-sciences-bursary/161081/
    ] http_request                   response_time_ms=2277.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=50'
    ] http_request                   response_time_ms=1971.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=49'
    ] http_request                   response_time_ms=12.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-open-to-vietnamese-students/139070/
    ] http_request                   response_time_ms=2139.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=51'
    ] http_request                   response_time_ms=2035.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=52'
    ] http_request                   response_time_ms=2273.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=50'
    ] http_request                   response_time_ms=1731.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=49'
    ] http_request                   response_time_ms=681.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=54'
    ] http_request                   response_time_ms=131.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/regional-excellence-scholarships/167682/
    ] http_request                   response_time_ms=955.1 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=56'
    ] http_request                   response_time_ms=2402.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=51'
    ] http_request                   response_time_ms=177.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/ul-family-alumni-scholarship/167749/
    ] http_request                   response_time_ms=263.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=52'
    ] http_request                   response_time_ms=55.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-postgraduate-taught-awards/164315/
    ] http_request                   response_time_ms=9.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-undergraduate-merit-awards/161100/
    ] http_request                   response_time_ms=1002.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=50'
    ] http_request                   response_time_ms=2195.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=50'
    ] http_request                   response_time_ms=1912.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=51'
    ] http_request                   response_time_ms=250.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/professor-brian-fynes-memorial-scholarship/148211/
    ] http_request                   response_time_ms=52.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-international-undergraduate-scholarships/166280/
    ] http_request                   response_time_ms=894.1 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=57'
    ] http_request                   response_time_ms=9.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/msc-law-and-finance-scholarship/166271/
    ] http_request                   response_time_ms=29.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=54'
    ] http_request                   response_time_ms=10.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-merit-scholarships/161082/
    ] http_request                   response_time_ms=1947.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=49'
    ] http_request                   response_time_ms=918.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=49'
    ] http_request                   response_time_ms=858.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=50'
    ] http_request                   response_time_ms=9.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-arts-celtic-studies-and-social-sciences-international-undergraduate-scholarships/166282/
    ] http_request                   response_time_ms=10.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/tus-global-scholarship-(previously-presidents-scholarship)/166289/
    ] http_request                   response_time_ms=2559.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=52'
    ] http_request                   response_time_ms=2431.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=53'
    ] http_request                   response_time_ms=716.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=53'
    ] http_request                   response_time_ms=634.5 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=58'
    ] http_request                   response_time_ms=41.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-humanities-and-social-sciences-bursary/161081/
    ] http_request                   response_time_ms=671.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=52'
    ] http_request                   response_time_ms=9.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-open-to-vietnamese-students/139070/
    ] http_request                   response_time_ms=2145.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=51'
    ] http_request                   response_time_ms=178.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/regional-excellence-scholarships/167682/
    ] http_request                   response_time_ms=2053.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=53'
    ] http_request                   response_time_ms=52.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/ul-family-alumni-scholarship/167749/
    ] http_request                   response_time_ms=2022.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=54'
    ] http_request                   response_time_ms=10.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-postgraduate-taught-awards/164315/
    ] http_request                   response_time_ms=52.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=57'
    ] http_request                   response_time_ms=1000.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=52'
    ] http_request                   response_time_ms=840.8 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=59'
    ] http_request                   response_time_ms=9.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-undergraduate-merit-awards/161100/
    ] http_request                   response_time_ms=1894.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=52'
    ] http_request                   response_time_ms=296.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/professor-brian-fynes-memorial-scholarship/148211/
    ] http_request                   response_time_ms=2441.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=51'
    ] http_request                   response_time_ms=1969.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=53'
    ] http_request                   response_time_ms=215.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-international-undergraduate-scholarships/166280/
    ] http_request                   response_time_ms=1913.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=54'
    ] http_request                   response_time_ms=213.9 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/msc-law-and-finance-scholarship/166271/
    ] http_request                   response_time_ms=949.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=52'
    ] http_request                   response_time_ms=53.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-merit-scholarships/161082/
    ] http_request                   response_time_ms=931.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=53'
    ] http_request                   response_time_ms=1943.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=53'
    ] http_request                   response_time_ms=9.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-arts-celtic-studies-and-social-sciences-international-undergraduate-scholarships/166282/
    ] http_request                   response_time_ms=10.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/tus-global-scholarship-(previously-presidents-scholarship)/166289/
    ] http_request                   response_time_ms=2070.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=54'
    ] http_request                   response_time_ms=1390.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=54'
    ] http_request                   response_time_ms=173.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-humanities-and-social-sciences-bursary/161081/
    ] http_request                   response_time_ms=2103.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=56'
    ] http_request                   response_time_ms=1799.0 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=60'
    ] http_request                   response_time_ms=913.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=54'
    ] listing_progress               collected=720 page=60 scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=115.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/msc-merit-based-scholarships-open-to-vietnamese-students/139070/
    ] http_request                   response_time_ms=296.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=52'
    ] http_request                   response_time_ms=2402.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=55'
    ] http_request                   response_time_ms=1023.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=55'
    ] http_request                   response_time_ms=129.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/regional-excellence-scholarships/167682/
    ] http_request                   response_time_ms=9.6 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-limerick/ul-family-alumni-scholarship/167749/
    ] http_request                   response_time_ms=9.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-arts-social-sciences-and-celtic-studies-postgraduate-taught-awards/164315/
    ] http_request                   response_time_ms=9.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-undergraduate-merit-awards/161100/
    ] http_request                   response_time_ms=10.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-dublin/professor-brian-fynes-memorial-scholarship/148211/
    ] http_request                   response_time_ms=8.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-business-and-law-international-undergraduate-scholarships/166280/
    ] http_request                   response_time_ms=9.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/msc-law-and-finance-scholarship/166271/
    ] http_request                   response_time_ms=1057.6 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=61'
    ] http_request                   response_time_ms=1794.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=57'
    ] http_request                   response_time_ms=1901.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=56'
    ] http_request                   response_time_ms=126.0 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-merit-scholarships/161082/
    ] http_request                   response_time_ms=9.4 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-college-cork/college-of-arts-celtic-studies-and-social-sciences-international-undergraduate-scholarships/166282/
    ] http_request                   response_time_ms=12.7 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/tus-global-scholarship-(previously-presidents-scholarship)/166289/
    ] http_request                   response_time_ms=8.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/dublin-city-university/dcu-humanities-and-social-sciences-bursary/161081/
    ] http_request                   response_time_ms=957.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=53'
    ] http_request                   response_time_ms=684.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=55'
    ] http_request                   response_time_ms=3393.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=52'
    ] http_request                   response_time_ms=3222.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=53'
    ] http_request                   response_time_ms=2055.2 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=54'
    ] http_request                   response_time_ms=1977.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=57'
    ] http_request                   response_time_ms=2180.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=55'
    ] http_request                   response_time_ms=2080.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=56'
    ] http_request                   response_time_ms=1894.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=56'
    ] http_request                   response_time_ms=1850.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=57'
    ] http_request                   response_time_ms=28.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=60'
    ] http_request                   response_time_ms=888.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=55'
    ] http_request                   response_time_ms=1876.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=52'
    ] http_request                   response_time_ms=1707.3 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=62'
    ] http_request                   response_time_ms=3009.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=53'
    ] http_request                   response_time_ms=2583.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=55'
    ] http_request                   response_time_ms=707.7 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=school&page=5'
    ] http_request                   response_time_ms=557.4 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=undergraduate&page=5'
    ] http_request                   response_time_ms=1481.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=57'
    ] http_request                   response_time_ms=2278.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=54'
    ] http_request                   response_time_ms=2304.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=57'
    ] http_request                   response_time_ms=2013.7 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=foundation&page=5'
    ] http_request                   response_time_ms=986.9 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=58'
    ] http_request                   response_time_ms=1804.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=56'
    ] http_request                   response_time_ms=1826.3 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=postgraduate&page=5'
    ] http_request                   response_time_ms=984.7 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=undergraduate&page=5'
    ] http_request                   response_time_ms=845.9 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=doctorate&page=5'
    ] http_request                   response_time_ms=2387.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=55'
    ] http_request                   response_time_ms=69.0 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=57'
    ] http_request                   response_time_ms=2599.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=56'
    ] http_request                   response_time_ms=2462.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=56'
    ] http_request                   response_time_ms=1922.3 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=57'
    ] http_request                   response_time_ms=253.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
    ] http_request                   response_time_ms=1747.2 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=postgraduate&page=5'
    ] http_request                   response_time_ms=1916.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=58'
    ] http_request                   response_time_ms=924.2 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
    ] http_request                   response_time_ms=1866.9 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=63'
    ] http_request                   response_time_ms=2111.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=59'
    ] http_request                   response_time_ms=926.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=56'
    ] http_request                   response_time_ms=1001.3 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
    ] http_request                   response_time_ms=1684.5 scraper=IDPScholarshipScraper status_code=200 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=pre-degree-vocational&page=5'
    ] http_request                   response_time_ms=813.8 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
    ] http_request                   response_time_ms=7.1 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=59'
    ] http_request                   response_time_ms=8.8 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=59'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
    ] http_request                   response_time_ms=1978.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=55'
    ] http_request                   response_time_ms=1075.4 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=59'
    ] http_request                   response_time_ms=7.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
    ] http_request                   response_time_ms=9.5 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=60'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=60'
    ] http_request                   response_time_ms=8.2 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=55'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=55'
    ] http_request                   response_time_ms=627.3 scraper=IDPScholarshipScraper status_code=200 url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
    ] http_request                   response_time_ms=2351.1 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=60'
    ] http_request                   response_time_ms=7.8 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
    ] http_request                   response_time_ms=1486.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=58'
    ] http_request                   response_time_ms=7.3 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=56'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=56'
    ] http_request                   response_time_ms=636.1 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
    ] http_request                   response_time_ms=2675.5 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=59'
    ] http_request                   response_time_ms=1034.7 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=57'
    ] http_request                   response_time_ms=935.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=58'
    ] http_request                   response_time_ms=100.4 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=57'
    ] http_request                   response_time_ms=101.7 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/canada/?page=57'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
Error:    ] combo_bulk_upsert_failed       combo=canada:postgraduate error="cannot import name 'bulk_upsert_courses' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPCourseScraper
    ] combo_complete                 combo=canada:postgraduate combo_seconds=89.8 found=648 progress=44.4% scraper=IDPCourseScraper total_so_far=648
    ] combo_start                    combo=united-states:postgraduate elapsed=90.0s progress=55.6% scraper=IDPCourseScraper
    ] http_request                   response_time_ms=8.5 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=58'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=58'
    ] http_request                   response_time_ms=7.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
    ] http_request                   response_time_ms=1523.6 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=55'
    ] http_request                   response_time_ms=8.1 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=59'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=59'
    ] http_request                   response_time_ms=8.1 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
    ] http_request                   response_time_ms=8.1 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=60'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-kingdom/?page=60'
Error:    ] combo_bulk_upsert_failed       combo=united-kingdom:undergraduate error="cannot import name 'bulk_upsert_courses' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPCourseScraper
    ] combo_complete                 combo=united-kingdom:undergraduate combo_seconds=90.0 found=684 progress=22.2% scraper=IDPCourseScraper total_so_far=1332
    ] combo_start                    combo=united-states:doctorate elapsed=90.0s progress=61.1% scraper=IDPCourseScraper
    ] http_request                   response_time_ms=6.9 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=58'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=58'
    ] http_request                   response_time_ms=1746.5 scraper=IDPScholarshipScraper status_code=200 url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
    ] http_request                   response_time_ms=6.4 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=59'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=59'
    ] http_request                   response_time_ms=1796.5 scraper=IDPUniversityScraper status_code=200 url='https://www.idp.com/nepal/find-a-university/?page=64'
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url='https://www.idp.com/nepal/find-a-university/?page=65'
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url='https://www.idp.com/nepal/find-a-university/?page=65'
Warning:  ] listing_fetch_failed           page=65 scraper=IDPUniversityScraper
    ] phase1_complete                scraper=IDPUniversityScraper total_stubs=768
    ] progress                       done=0 pct=0.0% scraper=IDPUniversityScraper total=768
    ] http_request                   response_time_ms=6.2 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=60'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/canada/?page=60'
Error:    ] combo_bulk_upsert_failed       combo=canada:doctorate error="cannot import name 'bulk_upsert_courses' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPCourseScraper
    ] combo_complete                 combo=canada:doctorate combo_seconds=89.8 found=684 progress=50.0% scraper=IDPCourseScraper total_so_far=2016
    ] combo_start                    combo=ireland:undergraduate elapsed=91.0s progress=66.7% scraper=IDPCourseScraper
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
    ] http_request                   response_time_ms=2337.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=60'
    ] http_request                   response_time_ms=128.0 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=58'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=58'
    ] http_request                   response_time_ms=8.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
    ] http_request                   response_time_ms=9.5 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=59'
    ] http_request                   response_time_ms=11.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/champlain-college-saint-lambert/IID-CA-01102/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=59'
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/champlain-college-saint-lambert/IID-CA-01102/
    ] http_request                   response_time_ms=6.8 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=60'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-kingdom/?page=60'
Error:    ] combo_bulk_upsert_failed       combo=united-kingdom:doctorate error="cannot import name 'bulk_upsert_courses' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPCourseScraper
    ] combo_complete                 combo=united-kingdom:doctorate combo_seconds=90.6 found=684 progress=33.3% scraper=IDPCourseScraper total_so_far=2700
    ] combo_start                    combo=ireland:postgraduate elapsed=91.0s progress=72.2% scraper=IDPCourseScraper
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
    ] http_request                   response_time_ms=6.5 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=61'
    ] http_request                   response_time_ms=8.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-english-language-centre-elc-eastbourne/IID-UK-03134/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=61'
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-english-language-centre-elc-eastbourne/IID-UK-03134/
    ] http_request                   response_time_ms=6.8 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=62'
    ] http_request                   response_time_ms=8.6 scraper=IDPScholarshipScraper status_code=403 url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=62'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
    ] http_request                   response_time_ms=7.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-english-language-centre-elc-chester/IID-UK-03136/
    ] http_request                   response_time_ms=8.0 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=63'
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-english-language-centre-elc-chester/IID-UK-03136/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/australia/?page=63'
Error:    ] combo_bulk_upsert_failed       combo=australia:doctorate error="cannot import name 'bulk_upsert_courses' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPCourseScraper
    ] combo_complete                 combo=australia:doctorate combo_seconds=90.9 found=720 progress=16.7% scraper=IDPCourseScraper total_so_far=3420
    ] combo_start                    combo=ireland:doctorate elapsed=91.0s progress=77.8% scraper=IDPCourseScraper
    ] http_request                   response_time_ms=2371.8 scraper=IDPCourseScraper status_code=200 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=56'
    ] http_request                   response_time_ms=136.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
    ] http_request                   response_time_ms=7.0 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=58'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=58'
    ] http_request                   response_time_ms=6.7 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
    ] http_request                   response_time_ms=7.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kings-education-united-kingdom/IID-UK-00864/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kings-education-united-kingdom/IID-UK-00864/
    ] http_request                   response_time_ms=7.2 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=59'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=59'
    ] http_request                   response_time_ms=7.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
    ] http_request                   response_time_ms=7.7 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=60'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/united-states/?page=60'
Error:    ] combo_bulk_upsert_failed       combo=united-states:undergraduate error="cannot import name 'bulk_upsert_courses' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPCourseScraper
    ] combo_complete                 combo=united-states:undergraduate combo_seconds=90.8 found=684 progress=55.6% scraper=IDPCourseScraper total_so_far=4104
    ] combo_start                    combo=new-zealand:undergraduate elapsed=92.0s progress=83.3% scraper=IDPCourseScraper
    ] http_request                   response_time_ms=5.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/niagara-college-toronto/IID-CA-01410/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/niagara-college-toronto/IID-CA-01410/
    ] http_request                   response_time_ms=7.5 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=61'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=61'
    ] http_request                   response_time_ms=6.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
    ] http_request                   response_time_ms=7.4 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=62'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=62'
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/acknowledge-creativity/IID-AU-01203/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/acknowledge-creativity/IID-AU-01203/
    ] http_request                   response_time_ms=6.8 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
    ] http_request                   response_time_ms=6.4 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=63'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/canada/?page=63'
Error:    ] combo_bulk_upsert_failed       combo=canada:undergraduate error="cannot import name 'bulk_upsert_courses' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPCourseScraper
    ] combo_complete                 combo=canada:undergraduate combo_seconds=91.6 found=720 progress=38.9% scraper=IDPCourseScraper total_so_far=4824
    ] combo_start                    combo=new-zealand:postgraduate elapsed=92.0s progress=88.9% scraper=IDPCourseScraper
    ] http_request                   response_time_ms=6.5 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=61'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=61'
    ] http_request                   response_time_ms=6.1 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
    ] http_request                   response_time_ms=8.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-culinary-collective/IID-NZ-01044/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-culinary-collective/IID-NZ-01044/
    ] http_request                   response_time_ms=7.0 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=62'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=62'
    ] http_request                   response_time_ms=6.6 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
    ] http_request                   response_time_ms=6.3 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=63'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-kingdom/?page=63'
Error:    ] combo_bulk_upsert_failed       combo=united-kingdom:postgraduate error="cannot import name 'bulk_upsert_courses' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPCourseScraper
    ] combo_complete                 combo=united-kingdom:postgraduate combo_seconds=91.9 found=696 progress=27.8% scraper=IDPCourseScraper total_so_far=5520
    ] combo_start                    combo=new-zealand:doctorate elapsed=92.0s progress=94.4% scraper=IDPCourseScraper
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/english-language-college-elc/IID-AU-00614/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/english-language-college-elc/IID-AU-00614/
    ] http_request                   response_time_ms=6.9 scraper=IDPCourseScraper status_code=403 url=https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-states/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url=https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-states/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
    ] http_request                   response_time_ms=6.2 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-states/?page=2'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-states/?page=2'
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/hawthorn-melbourne-english-language-centre/IID-AU-00547/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/hawthorn-melbourne-english-language-centre/IID-AU-00547/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
    ] http_request                   response_time_ms=6.7 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-states/?page=3'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/united-states/?page=3'
    ] combo_complete                 combo=united-states:postgraduate combo_seconds=2.4 found=0 progress=61.1% scraper=IDPCourseScraper total_so_far=5520
    ] http_request                   response_time_ms=6.6 scraper=IDPCourseScraper status_code=403 url=https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-states/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url=https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-states/
    ] http_request                   response_time_ms=7.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
    ] http_request                   response_time_ms=8.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/nova-scotia-community-college/IID-CA-01070/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/nova-scotia-community-college/IID-CA-01070/
    ] http_request                   response_time_ms=6.1 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-states/?page=2'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-states/?page=2'
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
    ] http_request                   response_time_ms=6.7 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-states/?page=3'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/united-states/?page=3'
    ] combo_complete                 combo=united-states:doctorate combo_seconds=2.5 found=0 progress=66.7% scraper=IDPCourseScraper total_so_far=5520
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/canberra-institute-of-technology/IID-AU-00364/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/canberra-institute-of-technology/IID-AU-00364/
    ] http_request                   response_time_ms=6.3 scraper=IDPCourseScraper status_code=403 url=https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/ireland/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url=https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/ireland/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
    ] http_request                   response_time_ms=6.4 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/ireland/?page=2'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/ireland/?page=2'
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/ec-english-language-centre-united-kingdom/IID-UK-00938/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/ec-english-language-centre-united-kingdom/IID-UK-00938/
    ] http_request                   response_time_ms=7.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
    ] http_request                   response_time_ms=6.5 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/ireland/?page=3'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/ireland/?page=3'
    ] combo_complete                 combo=ireland:undergraduate combo_seconds=2.5 found=0 progress=72.2% scraper=IDPCourseScraper total_so_far=5520
    ] http_request                   response_time_ms=6.8 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=61'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=61'
    ] http_request                   response_time_ms=6.4 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
    ] http_request                   response_time_ms=8.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-nebraska-at-omaha/IID-US-00985/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-nebraska-at-omaha/IID-US-00985/
    ] http_request                   response_time_ms=6.1 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=62'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=62'
    ] http_request                   response_time_ms=6.8 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
    ] http_request                   response_time_ms=6.9 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=63'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/australia/?page=63'
Error:    ] combo_bulk_upsert_failed       combo=australia:postgraduate error="cannot import name 'bulk_upsert_courses' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPCourseScraper
    ] combo_complete                 combo=australia:postgraduate combo_seconds=93.1 found=720 progress=11.1% scraper=IDPCourseScraper total_so_far=6240
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/ec-english-language-centre-united-kingdom/IID-UK-00938/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/ec-english-language-centre-united-kingdom/IID-UK-00938/
    ] http_request                   response_time_ms=6.6 scraper=IDPCourseScraper status_code=403 url=https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/ireland/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url=https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/ireland/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
    ] http_request                   response_time_ms=6.6 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/ireland/?page=2'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/ireland/?page=2'
    ] http_request                   response_time_ms=5.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/collins-academy-pty-ltd/IID-AU-02836/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/collins-academy-pty-ltd/IID-AU-02836/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
    ] http_request                   response_time_ms=6.2 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/ireland/?page=3'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/ireland/?page=3'
    ] combo_complete                 combo=ireland:postgraduate combo_seconds=2.8 found=0 progress=77.8% scraper=IDPCourseScraper total_so_far=6240
    ] http_request                   response_time_ms=7.5 scraper=IDPCourseScraper status_code=403 url=https://www.idp.com/nepal/find-a-course/all-subject/doctorate/ireland/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url=https://www.idp.com/nepal/find-a-course/all-subject/doctorate/ireland/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/mississippi-state-university/IID-US-00244/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/mississippi-state-university/IID-US-00244/
    ] http_request                   response_time_ms=6.6 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
    ] http_request                   response_time_ms=6.7 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/ireland/?page=2'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/ireland/?page=2'
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
    ] http_request                   response_time_ms=6.8 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/ireland/?page=3'
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/suny-oswego/IID-US-00032/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/ireland/?page=3'
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/suny-oswego/IID-US-00032/
    ] combo_complete                 combo=ireland:doctorate combo_seconds=2.8 found=0 progress=83.3% scraper=IDPCourseScraper total_so_far=6240
    ] http_request                   response_time_ms=6.2 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=58'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=58'
    ] http_request                   response_time_ms=6.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/canada-college/IID-CA-01264/
    ] http_request                   response_time_ms=8.6 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=59'
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/canada-college/IID-CA-01264/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=59'
    ] http_request                   response_time_ms=7.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
    ] http_request                   response_time_ms=6.6 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=60'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/australia/?page=60'
Error:    ] combo_bulk_upsert_failed       combo=australia:undergraduate error="cannot import name 'bulk_upsert_courses' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPCourseScraper
    ] combo_complete                 combo=australia:undergraduate combo_seconds=94.0 found=684 progress=5.6% scraper=IDPCourseScraper total_so_far=6924
    ] http_request                   response_time_ms=6.2 scraper=IDPCourseScraper status_code=403 url=https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/new-zealand/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url=https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/new-zealand/
    ] http_request                   response_time_ms=8.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lawrence-technological-university/IID-US-00066/
    ] http_request                   response_time_ms=6.9 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lawrence-technological-university/IID-US-00066/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
    ] http_request                   response_time_ms=7.0 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/new-zealand/?page=2'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/new-zealand/?page=2'
    ] http_request                   response_time_ms=6.6 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-state-university-fresno/IID-US-00006/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-state-university-fresno/IID-US-00006/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=13.3 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/new-zealand/?page=3'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/undergraduate/new-zealand/?page=3'
    ] combo_complete                 combo=new-zealand:undergraduate combo_seconds=3.0 found=0 progress=88.9% scraper=IDPCourseScraper total_so_far=6924
    ] http_request                   response_time_ms=7.3 scraper=IDPCourseScraper status_code=403 url=https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/new-zealand/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url=https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/new-zealand/
    ] http_request                   response_time_ms=7.9 scraper=IDPScholarshipScraper status_code=403 url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
    ] http_request                   response_time_ms=7.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/rhode-island-school-of-design/IID-US-00950/
    ] http_request                   response_time_ms=7.0 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/new-zealand/?page=2'
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/rhode-island-school-of-design/IID-US-00950/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/new-zealand/?page=2'
    ] http_request                   response_time_ms=6.6 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
    ] http_request                   response_time_ms=6.2 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/new-zealand/?page=3'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/postgraduate/new-zealand/?page=3'
    ] combo_complete                 combo=new-zealand:postgraduate combo_seconds=3.0 found=0 progress=94.4% scraper=IDPCourseScraper total_so_far=6924
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/duquesne-university/IID-US-00061/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/duquesne-university/IID-US-00061/
    ] http_request                   response_time_ms=6.8 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
    ] http_request                   response_time_ms=7.9 scraper=IDPCourseScraper status_code=403 url=https://www.idp.com/nepal/find-a-course/all-subject/doctorate/new-zealand/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url=https://www.idp.com/nepal/find-a-course/all-subject/doctorate/new-zealand/
    ] http_request                   response_time_ms=5.9 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/new-zealand/?page=2'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/new-zealand/?page=2'
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/james-madison-university-international-study-center-studygroup/IID-US-00238/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/james-madison-university-international-study-center-studygroup/IID-US-00238/
    ] http_request                   response_time_ms=6.2 scraper=IDPCourseScraper status_code=403 url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/new-zealand/?page=3'
Warning:  ] http_forbidden                 scraper=IDPCourseScraper url='https://www.idp.com/nepal/find-a-course/all-subject/doctorate/new-zealand/?page=3'
    ] combo_complete                 combo=new-zealand:doctorate combo_seconds=3.0 found=0 progress=100.0% scraper=IDPCourseScraper total_so_far=6924
    ] scrape_complete                elapsed_minutes=1.6 elapsed_seconds=95.2 scraper=IDPCourseScraper total_courses=6924
    ] scraper_complete               count=6924 scraper=idp_courses
    ] http_request                   response_time_ms=6.8 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/gonzaga-university-shorelight/IID-US-01349/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/gonzaga-university-shorelight/IID-US-01349/
    ] http_request                   response_time_ms=5.7 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/vanderbilt-university/IID-US-00297/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/vanderbilt-university/IID-US-00297/
    ] http_request                   response_time_ms=5.9 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
    ] http_request                   response_time_ms=6.6 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/los-medanos-college/IID-US-01076/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/los-medanos-college/IID-US-01076/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/james-cook-university-brisbane-operated-by-russo-higher-education/IID-AU-01250/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/james-cook-university-brisbane-operated-by-russo-higher-education/IID-AU-01250/
    ] http_request                   response_time_ms=7.8 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/queens-university-belfast-into-uk/IID-UK-01231/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/queens-university-belfast-into-uk/IID-UK-01231/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
    ] http_request                   response_time_ms=8.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-essex-international-college-kaplan-uk/IID-UK-01304/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-essex-international-college-kaplan-uk/IID-UK-01304/
    ] http_request                   response_time_ms=7.1 scraper=IDPScholarshipScraper status_code=403 url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/montclair-state-university-into-usa/IID-US-01560/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/montclair-state-university-into-usa/IID-US-01560/
    ] http_request                   response_time_ms=6.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-state-university-sacramento/IID-US-01128/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-state-university-sacramento/IID-US-01128/
    ] http_request                   response_time_ms=6.7 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
    ] http_request                   response_time_ms=7.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/texas-am-university-corpus-christi-international-study-center-studygroup/IID-US-01008/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/texas-am-university-corpus-christi-international-study-center-studygroup/IID-US-01008/
    ] http_request                   response_time_ms=7.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/dublin-international-foundation-college/IID-IE-02597/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/dublin-international-foundation-college/IID-IE-02597/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/canterbury-institute-of-management/IID-AU-01246/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/canterbury-institute-of-management/IID-AU-01246/
    ] http_request                   response_time_ms=6.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
    ] http_request                   response_time_ms=5.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/loyola-university-of-chicago/IID-US-00068/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/loyola-university-of-chicago/IID-US-00068/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-new-haven/IID-US-00987/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-new-haven/IID-US-00987/
    ] http_request                   response_time_ms=6.1 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/rivier-university/IID-US-00077/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/rivier-university/IID-US-00077/
    ] http_request                   response_time_ms=6.1 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
    ] http_request                   response_time_ms=6.4 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
    ] http_request                   response_time_ms=7.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-indianapolis/IID-US-00075/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-indianapolis/IID-US-00075/
    ] http_request                   response_time_ms=6.4 scraper=IDPScholarshipScraper status_code=403 url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/assiniboine-community-college/IID-CA-01194/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/assiniboine-community-college/IID-CA-01194/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-northern-british-columbia/IID-CA-00760/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-northern-british-columbia/IID-CA-00760/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=7.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
    ] http_request                   response_time_ms=6.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/wilmington-university/IID-US-02593/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/wilmington-university/IID-US-02593/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-houston/IID-US-00138/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-houston/IID-US-00138/
    ] http_request                   response_time_ms=6.1 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
    ] http_request                   response_time_ms=9.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cairns-college-of-english-and-business/IID-AU-01214/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cairns-college-of-english-and-business/IID-AU-01214/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/acadia-university/IID-CA-00637/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/acadia-university/IID-CA-00637/
    ] http_request                   response_time_ms=6.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/hillsborough-community-college/IID-US-00015/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/hillsborough-community-college/IID-US-00015/
    ] http_request                   response_time_ms=12.7 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
    ] http_request                   response_time_ms=7.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/rensselaer-polytechnic-institute-into/IID-US-03721/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/rensselaer-polytechnic-institute-into/IID-US-03721/
    ] http_request                   response_time_ms=7.1 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/gradability-pty-ltd-trading-as-performance-education/IID-AU-01457/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/gradability-pty-ltd-trading-as-performance-education/IID-AU-01457/
    ] http_request                   response_time_ms=7.2 scraper=IDPScholarshipScraper status_code=403 url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/old-dominion-university/IID-US-00087/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/old-dominion-university/IID-US-00087/
    ] http_request                   response_time_ms=6.1 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/florida-institute-of-technology/IID-US-00056/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/florida-institute-of-technology/IID-US-00056/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
    ] http_request                   response_time_ms=6.4 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/swinburne-university-of-technology-college/IID-AU-01359/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/swinburne-university-of-technology-college/IID-AU-01359/
    ] http_request                   response_time_ms=6.9 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lci-melbourne/IID-AU-01550/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lci-melbourne/IID-AU-01550/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/bright-world-education/IID-UK-01534/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/bright-world-education/IID-UK-01534/
    ] http_request                   response_time_ms=6.0 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
    ] http_request                   response_time_ms=6.8 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-business-public-policy-law-global-scholarships-region-based-undergraduate-scholarship/167683/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cllc-language-school/IID-CA-01036/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cllc-language-school/IID-CA-01036/
    ] http_request                   response_time_ms=7.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-information-technology-distinction-award/25673/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lci-language-schools/IID-CA-02512/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lci-language-schools/IID-CA-02512/
    ] http_request                   response_time_ms=6.9 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-psychology-distinction-award/118739/
    ] http_request                   response_time_ms=9.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/holmes-institute/IID-AU-00382/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/holmes-institute/IID-AU-00382/
    ] http_request                   response_time_ms=5.7 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/faculty-of-business-economics-and-accounting-distinction-award/92624/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/help-university/department-of-law-distinction-award/25706/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-baptist-university/IID-US-01558/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-baptist-university/IID-US-01558/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url="https://www.idp.com/scholarship/university-of-nottingham-malaysia/high-achiever's-scholarship-for-undergraduate-(new-students)/118741/"
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/bath-spa-university/IID-UK-00810/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/bath-spa-university/IID-UK-00810/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-of-galway/college-of-science-and-engineering-region-based-(usa)-idea-scholarship/164354/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/keele-university-international-college-navitas-uk/IID-UK-01425/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/keele-university-international-college-navitas-uk/IID-UK-01425/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/full-time-mba-regional-excellence-scholarship/139079/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin/equity-diversity-and-inclusion-scholarships-for-us-students/148190/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-hull/IID-UK-00783/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-hull/IID-UK-00783/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/technological-university-of-the-shannon:-midlands-midwest/nursing-scholarship/166288/
    ] http_request                   response_time_ms=8.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/international-college-of-management-sydney/IID-AU-00548/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/international-college-of-management-sydney/IID-AU-00548/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.1 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/university-college-dublin-international-study-centre/joint-scholarship/166277/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/boston-college/IID-US-00173/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/boston-college/IID-US-00173/
    ] http_request                   response_time_ms=6.7 scraper=IDPScholarshipScraper status_code=403 url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url=https://www.idp.com/scholarship/trinity-college-dublin-the-university-of-dublin/china-claddagh-postgraduate-scholarships/129936/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=school&page=6'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=school&page=6'
Warning:  ] page_fetch_failed              page=6 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=school&page=6'
Error:    ] combo_bulk_upsert_failed       combo=australia:school error="cannot import name 'bulk_upsert_scholarships' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPScholarshipScraper
    ] combo_complete                 combo=australia:school combo_seconds=102.8 found=60 progress=16.7% scraper=IDPScholarshipScraper total_so_far=60
    ] combo_start                    combo=uk:doctorate elapsed=103.0s progress=22.2% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-idaho/IID-US-00275/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-idaho/IID-US-00275/
    ] http_request                   response_time_ms=6.9 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=undergraduate&page=6'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=undergraduate&page=6'
Warning:  ] page_fetch_failed              page=6 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=undergraduate&page=6'
Error:    ] combo_bulk_upsert_failed       combo=australia:undergraduate error="cannot import name 'bulk_upsert_scholarships' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPScholarshipScraper
    ] combo_complete                 combo=australia:undergraduate combo_seconds=103.1 found=60 progress=2.8% scraper=IDPScholarshipScraper total_so_far=120
    ] combo_start                    combo=uk:foundation elapsed=103.0s progress=25.0% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/holmesglen-institute/IID-AU-00373/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/holmesglen-institute/IID-AU-00373/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=foundation&page=6'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=foundation&page=6'
Warning:  ] page_fetch_failed              page=6 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=foundation&page=6'
Error:    ] combo_bulk_upsert_failed       combo=australia:foundation error="cannot import name 'bulk_upsert_scholarships' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPScholarshipScraper
    ] combo_complete                 combo=australia:foundation combo_seconds=103.2 found=60 progress=11.1% scraper=IDPScholarshipScraper total_so_far=180
    ] combo_start                    combo=uk:pre-degree-vocational elapsed=103.0s progress=27.8% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/washington-state-university/IID-US-00095/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/washington-state-university/IID-US-00095/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=postgraduate&page=6'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=postgraduate&page=6'
Warning:  ] page_fetch_failed              page=6 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=postgraduate&page=6'
Error:    ] combo_bulk_upsert_failed       combo=australia:postgraduate error="cannot import name 'bulk_upsert_scholarships' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPScholarshipScraper
    ] combo_complete                 combo=australia:postgraduate combo_seconds=103.4 found=60 progress=5.6% scraper=IDPScholarshipScraper total_so_far=240
    ] combo_start                    combo=uk:school elapsed=103.0s progress=30.6% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.8 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=undergraduate&page=6'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=undergraduate&page=6'
Warning:  ] page_fetch_failed              page=6 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=undergraduate&page=6'
Error:    ] combo_bulk_upsert_failed       combo=uk:undergraduate error="cannot import name 'bulk_upsert_scholarships' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPScholarshipScraper
    ] combo_complete                 combo=uk:undergraduate combo_seconds=103.4 found=60 progress=19.4% scraper=IDPScholarshipScraper total_so_far=300
    ] combo_start                    combo=canada:undergraduate elapsed=104.0s progress=33.3% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=5.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/bond-university/IID-AU-00374/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/bond-university/IID-AU-00374/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=doctorate&page=6'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=doctorate&page=6'
Warning:  ] page_fetch_failed              page=6 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=doctorate&page=6'
Error:    ] combo_bulk_upsert_failed       combo=australia:doctorate error="cannot import name 'bulk_upsert_scholarships' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPScholarshipScraper
    ] combo_complete                 combo=australia:doctorate combo_seconds=103.6 found=60 progress=8.3% scraper=IDPScholarshipScraper total_so_far=360
    ] combo_start                    combo=canada:postgraduate elapsed=104.0s progress=36.1% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/charles-sturt-university-sydney-and-melbourne/IID-AU-01563/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/charles-sturt-university-sydney-and-melbourne/IID-AU-01563/
    ] http_request                   response_time_ms=7.4 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=postgraduate&page=6'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=postgraduate&page=6'
Warning:  ] page_fetch_failed              page=6 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=postgraduate&page=6'
Error:    ] combo_bulk_upsert_failed       combo=uk:postgraduate error="cannot import name 'bulk_upsert_scholarships' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPScholarshipScraper
    ] combo_complete                 combo=uk:postgraduate combo_seconds=103.7 found=60 progress=22.2% scraper=IDPScholarshipScraper total_so_far=420
    ] combo_start                    combo=canada:doctorate elapsed=104.0s progress=38.9% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-british-columbia-okanagan-campus/IID-CA-03522/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-british-columbia-okanagan-campus/IID-CA-03522/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=pre-degree-vocational&page=6'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=pre-degree-vocational&page=6'
Warning:  ] page_fetch_failed              page=6 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=pre-degree-vocational&page=6'
Error:    ] combo_bulk_upsert_failed       combo=australia:pre-degree-vocational error="cannot import name 'bulk_upsert_scholarships' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPScholarshipScraper
    ] combo_complete                 combo=australia:pre-degree-vocational combo_seconds=103.9 found=60 progress=13.9% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=canada:foundation elapsed=104.0s progress=41.7% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.7 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=doctorate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=doctorate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=doctorate'
    ] combo_complete                 combo=uk:doctorate combo_seconds=1.2 found=0 progress=25.0% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=canada:pre-degree-vocational elapsed=104.0s progress=44.4% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/syracuse-university/IID-US-00167/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/syracuse-university/IID-US-00167/
    ] http_request                   response_time_ms=6.4 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=foundation'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=foundation'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=foundation'
    ] combo_complete                 combo=uk:foundation combo_seconds=1.2 found=0 progress=27.8% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=canada:school elapsed=104.0s progress=47.2% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-wollongong-malaysia/IID-MY-03483/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-wollongong-malaysia/IID-MY-03483/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=pre-degree-vocational'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=pre-degree-vocational'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=pre-degree-vocational'
    ] combo_complete                 combo=uk:pre-degree-vocational combo_seconds=1.2 found=0 progress=30.6% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=usa:undergraduate elapsed=105.0s progress=50.0% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/hertfordshire-international-college-navitas-uk/IID-UK-01255/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/hertfordshire-international-college-navitas-uk/IID-UK-01255/
    ] http_request                   response_time_ms=6.6 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=school'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=school'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=uk&level=school'
    ] combo_complete                 combo=uk:school combo_seconds=1.2 found=0 progress=33.3% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=usa:postgraduate elapsed=105.0s progress=52.8% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.6 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=undergraduate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=undergraduate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=undergraduate'
    ] combo_complete                 combo=canada:undergraduate combo_seconds=1.2 found=0 progress=36.1% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=usa:doctorate elapsed=105.0s progress=55.6% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/english-language-centre-elc-bristol/IID-UK-00865/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/english-language-centre-elc-bristol/IID-UK-00865/
    ] http_request                   response_time_ms=6.1 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=postgraduate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=postgraduate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=postgraduate'
    ] combo_complete                 combo=canada:postgraduate combo_seconds=1.2 found=0 progress=38.9% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=usa:foundation elapsed=105.0s progress=58.3% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-reading-malaysia/IID-MY-03478/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-reading-malaysia/IID-MY-03478/
    ] http_request                   response_time_ms=6.0 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=doctorate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=doctorate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=doctorate'
    ] combo_complete                 combo=canada:doctorate combo_seconds=1.2 found=0 progress=41.7% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=usa:pre-degree-vocational elapsed=105.0s progress=61.1% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/auburn-university-shorelight/IID-US-00919/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/auburn-university-shorelight/IID-US-00919/
    ] http_request                   response_time_ms=5.9 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=foundation'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=foundation'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=foundation'
    ] combo_complete                 combo=canada:foundation combo_seconds=1.2 found=0 progress=44.4% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=usa:school elapsed=105.0s progress=63.9% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.4 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=pre-degree-vocational'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=pre-degree-vocational'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=pre-degree-vocational'
    ] combo_complete                 combo=canada:pre-degree-vocational combo_seconds=1.2 found=0 progress=47.2% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=ireland:undergraduate elapsed=105.0s progress=66.7% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/griffith-college-ireland/IID-IE-01207/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/griffith-college-ireland/IID-IE-01207/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=school'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=school'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=canada&level=school'
    ] combo_complete                 combo=canada:school combo_seconds=1.2 found=0 progress=50.0% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=ireland:postgraduate elapsed=106.0s progress=69.4% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lehigh-university/IID-US-00108/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lehigh-university/IID-US-00108/
    ] http_request                   response_time_ms=6.6 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=undergraduate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=undergraduate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=undergraduate'
    ] combo_complete                 combo=usa:undergraduate combo_seconds=1.2 found=0 progress=52.8% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=ireland:doctorate elapsed=106.0s progress=72.2% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=5.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/uwe-bristols-international-college-kaplan-uk/IID-UK-01306/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/uwe-bristols-international-college-kaplan-uk/IID-UK-01306/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=postgraduate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=postgraduate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=postgraduate'
    ] combo_complete                 combo=usa:postgraduate combo_seconds=1.2 found=0 progress=55.6% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=ireland:foundation elapsed=106.0s progress=75.0% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=doctorate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=doctorate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=doctorate'
    ] combo_complete                 combo=usa:doctorate combo_seconds=1.2 found=0 progress=58.3% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=ireland:pre-degree-vocational elapsed=106.0s progress=77.8% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/glasgow-international-college-kaplan-uk/IID-UK-01298/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/glasgow-international-college-kaplan-uk/IID-UK-01298/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=foundation'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=foundation'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=foundation'
    ] combo_complete                 combo=usa:foundation combo_seconds=1.2 found=0 progress=61.1% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=ireland:school elapsed=106.0s progress=80.6% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/wilfrid-laurier-international-college/IID-CA-01386/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/wilfrid-laurier-international-college/IID-CA-01386/
    ] http_request                   response_time_ms=7.0 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=pre-degree-vocational'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=pre-degree-vocational'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=pre-degree-vocational'
    ] combo_complete                 combo=usa:pre-degree-vocational combo_seconds=1.2 found=0 progress=63.9% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=new-zealand:undergraduate elapsed=106.0s progress=83.3% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cuny-queens-college-navitas-usa/IID-US-01217/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cuny-queens-college-navitas-usa/IID-US-01217/
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=school'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=school'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=usa&level=school'
    ] combo_complete                 combo=usa:school combo_seconds=1.2 found=0 progress=66.7% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=new-zealand:postgraduate elapsed=106.0s progress=86.1% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.2 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=undergraduate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=undergraduate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=undergraduate'
    ] combo_complete                 combo=ireland:undergraduate combo_seconds=1.2 found=0 progress=69.4% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=new-zealand:doctorate elapsed=107.0s progress=88.9% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/royal-roads-university/IID-CA-00648/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/royal-roads-university/IID-CA-00648/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.4 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=postgraduate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=postgraduate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=postgraduate'
    ] combo_complete                 combo=ireland:postgraduate combo_seconds=1.2 found=0 progress=72.2% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=new-zealand:foundation elapsed=107.0s progress=91.7% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=7.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/new-brunswick-community-college/IID-CA-01073/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/new-brunswick-community-college/IID-CA-01073/
    ] http_request                   response_time_ms=6.9 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=doctorate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=doctorate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=doctorate'
    ] combo_complete                 combo=ireland:doctorate combo_seconds=1.2 found=0 progress=75.0% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=new-zealand:pre-degree-vocational elapsed=107.0s progress=94.4% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/taylors-college/IID-AU-01292/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/taylors-college/IID-AU-01292/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=foundation'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=foundation'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=foundation'
    ] combo_complete                 combo=ireland:foundation combo_seconds=1.2 found=0 progress=77.8% scraper=IDPScholarshipScraper total_so_far=480
    ] combo_start                    combo=new-zealand:school elapsed=107.0s progress=97.2% scraper=IDPScholarshipScraper
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=pre-degree-vocational'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=pre-degree-vocational'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=pre-degree-vocational'
    ] combo_complete                 combo=ireland:pre-degree-vocational combo_seconds=1.2 found=0 progress=80.6% scraper=IDPScholarshipScraper total_so_far=480
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/mount-royal-university/IID-CA-00738/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/mount-royal-university/IID-CA-00738/
    ] http_request                   response_time_ms=6.4 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=school'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=school'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=ireland&level=school'
    ] combo_complete                 combo=ireland:school combo_seconds=1.2 found=0 progress=83.3% scraper=IDPScholarshipScraper total_so_far=480
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-michigan-flint/IID-US-00976/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-michigan-flint/IID-US-00976/
    ] http_request                   response_time_ms=6.9 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=undergraduate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=undergraduate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=undergraduate'
    ] combo_complete                 combo=new-zealand:undergraduate combo_seconds=1.2 found=0 progress=86.1% scraper=IDPScholarshipScraper total_so_far=480
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/medicine-hat-college/IID-CA-03588/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/medicine-hat-college/IID-CA-03588/
    ] http_request                   response_time_ms=6.6 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=postgraduate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=postgraduate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=postgraduate'
    ] combo_complete                 combo=new-zealand:postgraduate combo_seconds=1.2 found=0 progress=88.9% scraper=IDPScholarshipScraper total_so_far=480
    ] http_request                   response_time_ms=6.7 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=doctorate'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=doctorate'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=doctorate'
    ] combo_complete                 combo=new-zealand:doctorate combo_seconds=1.2 found=0 progress=91.7% scraper=IDPScholarshipScraper total_so_far=480
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/london-school-of-hygiene-tropical-medicine-university-of-london/IID-UK-02633/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/london-school-of-hygiene-tropical-medicine-university-of-london/IID-UK-02633/
    ] http_request                   response_time_ms=6.5 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=foundation'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=foundation'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=foundation'
    ] combo_complete                 combo=new-zealand:foundation combo_seconds=1.2 found=0 progress=94.4% scraper=IDPScholarshipScraper total_so_far=480
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/adelaide-university/IID-AU-01591/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/adelaide-university/IID-AU-01591/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=pre-degree-vocational'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=pre-degree-vocational'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=pre-degree-vocational'
    ] combo_complete                 combo=new-zealand:pre-degree-vocational combo_seconds=1.2 found=0 progress=97.2% scraper=IDPScholarshipScraper total_so_far=480
    ] http_request                   response_time_ms=5.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/western-sydney-university-international-college/IID-AU-01278/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/western-sydney-university-international-college/IID-AU-01278/
    ] http_request                   response_time_ms=6.3 scraper=IDPScholarshipScraper status_code=403 url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=school'
Warning:  ] http_forbidden                 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=school'
Warning:  ] page_fetch_failed              page=1 scraper=IDPScholarshipScraper url='https://www.idp.com/nepal/find-a-scholarship/?country=new-zealand&level=school'
    ] combo_complete                 combo=new-zealand:school combo_seconds=1.2 found=0 progress=100.0% scraper=IDPScholarshipScraper total_so_far=480
    ] scrape_complete                elapsed_minutes=1.8 scraper=IDPScholarshipScraper total=480
    ] scraper_complete               count=480 scraper=idp_scholarships
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/nova-southeastern-university-eag/IID-US-01239/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/nova-southeastern-university-eag/IID-US-01239/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/buckinghamshire-new-university/IID-UK-01543/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/buckinghamshire-new-university/IID-UK-01543/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-academy-92-ua92/IID-UK-01382/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-academy-92-ua92/IID-UK-01382/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/murdoch-college/IID-AU-01464/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/murdoch-college/IID-AU-01464/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/college-of-new-caledonia/IID-CA-01057/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/college-of-new-caledonia/IID-CA-01057/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/saskatchewan-polytechnic/IID-CA-00639/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/saskatchewan-polytechnic/IID-CA-00639/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/justice-institute-of-british-columbia/IID-CA-02591/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/justice-institute-of-british-columbia/IID-CA-02591/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-canberra/IID-AU-00430/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-canberra/IID-AU-00430/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/middle-tennessee-state-university/IID-US-02799/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/middle-tennessee-state-university/IID-US-02799/
    ] http_request                   response_time_ms=8.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-the-west-of-scotland/IID-UK-01444/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-the-west-of-scotland/IID-UK-01444/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/foothill-college/IID-US-00009/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/foothill-college/IID-US-00009/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/camosun-college/IID-CA-00642/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/camosun-college/IID-CA-00642/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] progress                       done=100 pct=13.0% scraper=IDPUniversityScraper total=768
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/la-trobe-university/IID-AU-00406/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/la-trobe-university/IID-AU-00406/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-alabama-birmingham-into-usa/IID-US-01174/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-alabama-birmingham-into-usa/IID-US-01174/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-wolverhampton/IID-UK-00803/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-wolverhampton/IID-UK-00803/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/trent-university/IID-CA-00640/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/trent-university/IID-CA-00640/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/salford-college/IID-AU-01322/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/salford-college/IID-AU-01322/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/technological-university-dublin/IID-IE-01124/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/technological-university-dublin/IID-IE-01124/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/bishops-university/IID-CA-00714/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/bishops-university/IID-CA-00714/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/confederation-college-of-applied-arts-and-technology/IID-CA-00723/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/confederation-college-of-applied-arts-and-technology/IID-CA-00723/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/minnesota-state-university-mankato/IID-US-00960/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/minnesota-state-university-mankato/IID-US-00960/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/fanshawe-college/IID-CA-00725/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/fanshawe-college/IID-CA-00725/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/york-university/IID-CA-00712/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/york-university/IID-CA-00712/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/wayne-state-university/IID-US-00300/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/wayne-state-university/IID-US-00300/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/scu-college/IID-AU-00557/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/scu-college/IID-AU-00557/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/pratt-institute/IID-US-00089/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/pratt-institute/IID-US-00089/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-australian-national-university/IID-AU-00410/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-australian-national-university/IID-AU-00410/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sae-university-college/IID-AU-00636/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sae-university-college/IID-AU-00636/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/taylors-university/IID-MY-03480/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/taylors-university/IID-MY-03480/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-nebraska-lincoln/IID-US-00284/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-nebraska-lincoln/IID-US-00284/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-toledo/IID-US-00166/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-toledo/IID-US-00166/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northern-kentucky-university/IID-US-00081/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northern-kentucky-university/IID-US-00081/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/justice-institute-of-british-columbia/IID-CA-02591/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/justice-institute-of-british-columbia/IID-CA-02591/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-canberra/IID-AU-00430/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-canberra/IID-AU-00430/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/middle-tennessee-state-university/IID-US-02799/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/middle-tennessee-state-university/IID-US-02799/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-the-west-of-scotland/IID-UK-01444/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-the-west-of-scotland/IID-UK-01444/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/foothill-college/IID-US-00009/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/foothill-college/IID-US-00009/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/camosun-college/IID-CA-00642/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/camosun-college/IID-CA-00642/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/la-trobe-university/IID-AU-00406/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/la-trobe-university/IID-AU-00406/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sae-university-college/IID-AU-00636/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sae-university-college/IID-AU-00636/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/seattle-central-college/IID-US-00019/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/seattle-central-college/IID-US-00019/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-waikato/IID-NZ-00822/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-waikato/IID-NZ-00822/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/technological-university-dublin/IID-IE-01124/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/technological-university-dublin/IID-IE-01124/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/bishops-university/IID-CA-00714/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/bishops-university/IID-CA-00714/
    ] http_request                   response_time_ms=7.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/bond-university/IID-AU-00374/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/bond-university/IID-AU-00374/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/newcastle-university/IID-UK-00665/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/newcastle-university/IID-UK-00665/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-waikato/IID-NZ-00822/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-waikato/IID-NZ-00822/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/hertfordshire-international-college-navitas-uk/IID-UK-01255/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/hertfordshire-international-college-navitas-uk/IID-UK-01255/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/pratt-institute/IID-US-00089/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/pratt-institute/IID-US-00089/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/seattle-central-college/IID-US-00019/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/seattle-central-college/IID-US-00019/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lawrence-technological-university/IID-US-00066/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lawrence-technological-university/IID-US-00066/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/houston-city-college/IID-US-04099/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/houston-city-college/IID-US-04099/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/hillsborough-community-college/IID-US-00015/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/hillsborough-community-college/IID-US-00015/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/apple-study-group/IID-AU-00629/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/apple-study-group/IID-AU-00629/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/investin-dukes-education/IID-UK-03301/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/investin-dukes-education/IID-UK-03301/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/mount-allison-university/IID-CA-01093/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/mount-allison-university/IID-CA-01093/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/college-of-william-and-mary/IID-US-00229/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/college-of-william-and-mary/IID-US-00229/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/international-sport-college-of-australia/IID-AU-01296/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/international-sport-college-of-australia/IID-AU-01296/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/trinity-college/IID-AU-00510/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/trinity-college/IID-AU-00510/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/front-cooking-school/IID-AU-01202/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/front-cooking-school/IID-AU-01202/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/liverpool-international-college-kaplan-uk/IID-UK-01300/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/liverpool-international-college-kaplan-uk/IID-UK-01300/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cats-stafford-house/IID-UK-01418/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cats-stafford-house/IID-UK-01418/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/international-language-academy-of-canada-ilac/IID-CA-00913/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/international-language-academy-of-canada-ilac/IID-CA-00913/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/aston-university-london-campus-ceg/IID-UK-02968/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/aston-university-london-campus-ceg/IID-UK-02968/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/florida-state-university/IID-US-00121/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/florida-state-university/IID-US-00121/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-california-santa-cruz/IID-US-00186/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-california-santa-cruz/IID-US-00186/
    ] http_request                   response_time_ms=8.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/san-francisco-state-university/IID-US-00952/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/san-francisco-state-university/IID-US-00952/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/simmons-university-kaplan-international/IID-US-01337/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/simmons-university-kaplan-international/IID-US-01337/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/canada-college-usa/IID-US-01276/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/canada-college-usa/IID-US-01276/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/long-island-university-cw-post/IID-US-00070/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/long-island-university-cw-post/IID-US-00070/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/midwestern-state-university/IID-US-00973/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/midwestern-state-university/IID-US-00973/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/irvine-valley-college/IID-US-01266/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/irvine-valley-college/IID-US-01266/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/nova-scotia-college-of-art-and-design-nscad-university/IID-CA-01009/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/nova-scotia-college-of-art-and-design-nscad-university/IID-CA-01009/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/white-house-guardians/IID-UK-01492/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/white-house-guardians/IID-UK-01492/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/marquette-university/IID-US-00242/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/marquette-university/IID-US-00242/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/fairleigh-dickinson-university-united-states/IID-US-00980/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/fairleigh-dickinson-university-united-states/IID-US-00980/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-hartford-studygroup-usa/IID-US-01241/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-hartford-studygroup-usa/IID-US-01241/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/american-collegiate-live-shorelight/IID-US-01279/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/american-collegiate-live-shorelight/IID-US-01279/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cornell-university/IID-US-00232/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cornell-university/IID-US-00232/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/towson-university-study-group/IID-US-01606/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/towson-university-study-group/IID-US-01606/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-texas-austin/IID-US-00292/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-texas-austin/IID-US-00292/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/towson-university-study-group/IID-US-01606/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/towson-university-study-group/IID-US-01606/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-niagara-falls/IID-CA-01569/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-niagara-falls/IID-CA-01569/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-hotel-school/IID-AU-00556/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-hotel-school/IID-AU-00556/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/pennsylvania-state-university-university-park/IID-US-00254/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/pennsylvania-state-university-university-park/IID-US-00254/
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lewis-university/IID-US-01585/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lewis-university/IID-US-01585/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/nyu-tandon-school-of-engineering/IID-US-00176/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/nyu-tandon-school-of-engineering/IID-US-00176/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/olds-college-of-agriculture-technology/IID-CA-03489/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/olds-college-of-agriculture-technology/IID-CA-03489/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-north-carolina-at-greensboro/IID-US-00208/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-north-carolina-at-greensboro/IID-US-00208/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-state-university-east-bay/IID-US-00946/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-state-university-east-bay/IID-US-00946/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/henley-business-school/IID-UK-03555/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/henley-business-school/IID-UK-03555/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/eastern-institute-of-technology/IID-NZ-01055/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/eastern-institute-of-technology/IID-NZ-01055/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-michigan-ann-arbor/IID-US-00281/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-michigan-ann-arbor/IID-US-00281/
    ] http_request                   response_time_ms=7.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/west-virginia-university/IID-US-00204/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/west-virginia-university/IID-US-00204/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-new-mexico/IID-US-00285/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-new-mexico/IID-US-00285/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/trinity-college-dublin-the-university-of-dublin/IID-IE-01116/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/trinity-college-dublin-the-university-of-dublin/IID-IE-01116/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/national-college-of-ireland/IID-IE-01191/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/national-college-of-ireland/IID-IE-01191/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/roosevelt-university-chicago/IID-US-02592/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/roosevelt-university-chicago/IID-US-02592/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-maryland-baltimore-county/IID-US-00216/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-maryland-baltimore-county/IID-US-00216/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lancaster-university-leipzig-navitas-uk/IID-UK-01383/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lancaster-university-leipzig-navitas-uk/IID-UK-01383/
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-the-pacific-shorelight/IID-US-01018/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-the-pacific-shorelight/IID-US-01018/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/glasgow-school-of-art/IID-UK-01015/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/glasgow-school-of-art/IID-UK-01015/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/nipissing-university/IID-CA-01325/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/nipissing-university/IID-CA-01325/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-chichester/IID-UK-01448/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-chichester/IID-UK-01448/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sp-jain-london-school-of-management/IID-UK-02699/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sp-jain-london-school-of-management/IID-UK-02699/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/st-lawrence-college/IID-CA-00649/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/st-lawrence-college/IID-CA-00649/
    ] http_request                   response_time_ms=117.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-windsor/IID-CA-00767/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-windsor/IID-CA-00767/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/baxter-institute/IID-AU-00597/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/baxter-institute/IID-AU-00597/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/claremont-graduate-university-cgu/IID-US-01215/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/claremont-graduate-university-cgu/IID-US-01215/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cape-breton-university/IID-CA-00921/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cape-breton-university/IID-CA-00921/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/new-york-university-nyu-school-of-professional-studies/IID-US-01555/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/new-york-university-nyu-school-of-professional-studies/IID-US-01555/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/london-school-of-economics-and-political-science-university-of-london/IID-UK-01024/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/london-school-of-economics-and-political-science-university-of-london/IID-UK-01024/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] progress                       done=200 pct=26.0% scraper=IDPUniversityScraper total=768
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/toi-ohomai-institute-of-technology/IID-NZ-00834/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/toi-ohomai-institute-of-technology/IID-NZ-00834/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-state-university-san-marcos/IID-US-00931/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-state-university-san-marcos/IID-US-00931/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/phoenix-academy/IID-AU-00388/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/phoenix-academy/IID-AU-00388/
    ] http_request                   response_time_ms=10.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/new-york-university/IID-US-00247/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/new-york-university/IID-US-00247/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/australian-learning-group-pty-ltd/IID-AU-02508/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/australian-learning-group-pty-ltd/IID-AU-02508/
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sydney-english-language-academy/IID-AU-00836/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sydney-english-language-academy/IID-AU-00836/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/apm-college-of-business-and-communication/IID-AU-00769/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/apm-college-of-business-and-communication/IID-AU-00769/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kingston-university-london-isc-study-group-uk/IID-UK-01363/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kingston-university-london-isc-study-group-uk/IID-UK-01363/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/suny-university-at-albany/IID-US-00184/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/suny-university-at-albany/IID-US-00184/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-massachusetts-dartmouth/IID-US-00042/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-massachusetts-dartmouth/IID-US-00042/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-huddersfield-isc-study-group-uk/IID-UK-01362/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-huddersfield-isc-study-group-uk/IID-UK-01362/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/thompson-rivers-university/IID-CA-00752/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/thompson-rivers-university/IID-CA-00752/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-rhode-island/IID-US-00130/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-rhode-island/IID-US-00130/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/royal-welsh-college-of-music-and-drama/IID-UK-00801/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/royal-welsh-college-of-music-and-drama/IID-UK-00801/
    ] http_request                   response_time_ms=7.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-akron/IID-US-00221/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-akron/IID-US-00221/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/solent-university-qa-higher-education/IID-UK-01312/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/solent-university-qa-higher-education/IID-UK-01312/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/elc-career-college/IID-AU-00384/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/elc-career-college/IID-AU-00384/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-notre-dame-australia/IID-AU-01068/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-notre-dame-australia/IID-AU-01068/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/south-dakota-state-university/IID-US-00260/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/south-dakota-state-university/IID-US-00260/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/aih-higher-education/IID-AU-00357/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/aih-higher-education/IID-AU-00357/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/tufts-university/IID-US-00084/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/tufts-university/IID-US-00084/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/nzist-trading-as-whitireia-and-weltech/IID-NZ-00830/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/nzist-trading-as-whitireia-and-weltech/IID-NZ-00830/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-missouri-kansas-city/IID-US-00148/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-missouri-kansas-city/IID-US-00148/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/queen-margaret-university-edinburgh/IID-UK-01440/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/queen-margaret-university-edinburgh/IID-UK-01440/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/excelsia-university-college/IID-AU-01125/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/excelsia-university-college/IID-AU-01125/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/edinburgh-napier-university/IID-UK-00799/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/edinburgh-napier-university/IID-UK-00799/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/ulster-university/IID-UK-01209/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/ulster-university/IID-UK-01209/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/uts-college/IID-AU-00515/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/uts-college/IID-AU-00515/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sae-auckland-navitas/IID-NZ-01549/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sae-auckland-navitas/IID-NZ-01549/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/istituto-marangoni-london/IID-UK-01445/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/istituto-marangoni-london/IID-UK-01445/
    ] http_request                   response_time_ms=7.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/humber-polytechnic/IID-CA-00730/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/humber-polytechnic/IID-CA-00730/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-new-hampshire/IID-US-00123/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-new-hampshire/IID-US-00123/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-new-brunswick/IID-CA-00759/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-new-brunswick/IID-CA-00759/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-miramar-university/IID-US-03828/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-miramar-university/IID-US-03828/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northwest-vista-college-alamo-colleges/IID-US-00313/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northwest-vista-college-alamo-colleges/IID-US-00313/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/orange-coast-college/IID-US-01531/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/orange-coast-college/IID-US-01531/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-york/IID-UK-00710/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-york/IID-UK-00710/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/melbourne-polytechnic/IID-AU-00512/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/melbourne-polytechnic/IID-AU-00512/
    ] http_request                   response_time_ms=7.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/robert-gordon-university/IID-UK-00798/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/robert-gordon-university/IID-UK-00798/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sault-college/IID-CA-01063/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sault-college/IID-CA-01063/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/melbourne-polytechnic/IID-AU-00512/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/melbourne-polytechnic/IID-AU-00512/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/robert-gordon-university/IID-UK-00798/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/robert-gordon-university/IID-UK-00798/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sault-college/IID-CA-01063/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sault-college/IID-CA-01063/
    ] http_request                   response_time_ms=7.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/le-cordon-bleu-australia/IID-AU-00570/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/le-cordon-bleu-australia/IID-AU-00570/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/goldsmiths-university-of-london/IID-UK-00688/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/goldsmiths-university-of-london/IID-UK-00688/
    ] http_request                   response_time_ms=8.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/uc-international-college-ucic/IID-NZ-00916/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/uc-international-college-ucic/IID-NZ-00916/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-st-andrews/IID-UK-00696/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-st-andrews/IID-UK-00696/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/selkirk-college/IID-CA-00747/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/selkirk-college/IID-CA-00747/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-the-highlands-and-islands-uhi/IID-UK-01610/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-the-highlands-and-islands-uhi/IID-UK-01610/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/simon-fraser-university/IID-CA-00749/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/simon-fraser-university/IID-CA-00749/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/macewan-university/IID-CA-00729/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/macewan-university/IID-CA-00729/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-nottingham/IID-UK-00708/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-nottingham/IID-UK-00708/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-nottingham/IID-UK-00708/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-nottingham/IID-UK-00708/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/new-zealand-tertiary-college/IID-NZ-01020/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/new-zealand-tertiary-college/IID-NZ-01020/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/academies-australasia/IID-AU-01087/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/academies-australasia/IID-AU-01087/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lakeland-college/IID-CA-01062/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lakeland-college/IID-CA-01062/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/oxford-brookes-university/IID-UK-00706/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/oxford-brookes-university/IID-UK-00706/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-west-london/IID-UK-00809/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-west-london/IID-UK-00809/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/unsw-college/IID-AU-00633/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/unsw-college/IID-AU-00633/
    ] http_request                   response_time_ms=8.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-delaware/IID-US-00202/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-delaware/IID-US-00202/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/bristol-uwe/IID-UK-00793/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/bristol-uwe/IID-UK-00793/
    ] http_request                   response_time_ms=7.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/western-sydney-university-the-college/IID-AU-00521/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/western-sydney-university-the-college/IID-AU-00521/
    ] http_request                   response_time_ms=7.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/north-island-college/IID-CA-01011/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/north-island-college/IID-CA-01011/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/london-south-bank-university/IID-UK-01436/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/london-south-bank-university/IID-UK-01436/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/charlton-brown/IID-AU-00606/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/charlton-brown/IID-AU-00606/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-strathclyde/IID-UK-00675/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-strathclyde/IID-UK-00675/
    ] http_request                   response_time_ms=9.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/edge-hill-university/IID-UK-01450/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/edge-hill-university/IID-UK-01450/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sunway-college-kl/IID-MY-03488/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sunway-college-kl/IID-MY-03488/
    ] http_request                   response_time_ms=8.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/charles-sturt-university/IID-AU-00368/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/charles-sturt-university/IID-AU-00368/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/heriot-watt-university/IID-UK-00785/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/heriot-watt-university/IID-UK-00785/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/menzies-institute-of-technology/IID-AU-00626/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/menzies-institute-of-technology/IID-AU-00626/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/uow-college/IID-AU-00386/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/uow-college/IID-AU-00386/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/aviron-quebec-college-technique/IID-CA-01351/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/aviron-quebec-college-technique/IID-CA-01351/
    ] http_request                   response_time_ms=9.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-illinois-urbana-champaign/IID-US-00125/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-illinois-urbana-champaign/IID-US-00125/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/canterbury-technical-institute/IID-AU-00631/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/canterbury-technical-institute/IID-AU-00631/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kent-institute-australia/IID-AU-00426/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kent-institute-australia/IID-AU-00426/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/stanford-university/IID-US-00182/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/stanford-university/IID-US-00182/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-colorado-boulder/IID-US-00217/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-colorado-boulder/IID-US-00217/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-alaska-fairbanks/IID-US-00215/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-alaska-fairbanks/IID-US-00215/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-southern-queensland-unisq/IID-AU-00440/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-southern-queensland-unisq/IID-AU-00440/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=7.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-south-wales/IID-UK-00802/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-south-wales/IID-UK-00802/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-arizona/IID-US-00162/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-arizona/IID-US-00162/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-new-england/IID-AU-00367/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-new-england/IID-AU-00367/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-college-cork/IID-IE-01121/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-college-cork/IID-IE-01121/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-manitoba/IID-CA-00758/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-manitoba/IID-CA-00758/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/liverpool-hope-university/IID-UK-01438/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/liverpool-hope-university/IID-UK-01438/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/baylor-university/IID-US-00144/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/baylor-university/IID-US-00144/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-missouri/IID-US-00175/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-missouri/IID-US-00175/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/teesside-university/IID-UK-00670/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/teesside-university/IID-UK-00670/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-massachusetts-boston-shorelight/IID-US-01110/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-massachusetts-boston-shorelight/IID-US-01110/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-exeter/IID-UK-00671/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-exeter/IID-UK-00671/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/liverpool-john-moores-university/IID-UK-00674/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/liverpool-john-moores-university/IID-UK-00674/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/montana-state-university/IID-US-00159/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/montana-state-university/IID-US-00159/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-north-carolina-charlotte/IID-US-00134/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-north-carolina-charlotte/IID-US-00134/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-south-florida/IID-US-00160/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-south-florida/IID-US-00160/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/auckland-university-of-technology/IID-NZ-00812/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/auckland-university-of-technology/IID-NZ-00812/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-kent/IID-UK-00677/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-kent/IID-UK-00677/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northeastern-university/IID-US-00146/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northeastern-university/IID-US-00146/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-chester/IID-UK-01321/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-chester/IID-UK-01321/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/curtin-university/IID-AU-00447/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/curtin-university/IID-AU-00447/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] progress                       done=300 pct=39.1% scraper=IDPUniversityScraper total=768
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-south-florida/IID-US-00160/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-south-florida/IID-US-00160/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-chester/IID-UK-01321/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-chester/IID-UK-01321/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cegep-de-la-gaspesie-et-des-iles/IID-CA-01108/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cegep-de-la-gaspesie-et-des-iles/IID-CA-01108/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-texas-dallas/IID-US-00132/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-texas-dallas/IID-US-00132/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/toronto-film-school/IID-CA-01071/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/toronto-film-school/IID-CA-01071/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northumbria-university-qa-higher-education/IID-UK-01309/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northumbria-university-qa-higher-education/IID-UK-01309/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-california-riverside-extension/IID-US-01195/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-california-riverside-extension/IID-US-01195/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/nottingham-trent-international-kaplan-uk/IID-UK-01301/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/nottingham-trent-international-kaplan-uk/IID-UK-01301/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/birmingham-city-university-international-college-navitas-uk/IID-UK-01260/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/birmingham-city-university-international-college-navitas-uk/IID-UK-01260/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/emily-carr-university-of-art-and-design/IID-CA-00724/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/emily-carr-university-of-art-and-design/IID-CA-00724/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/manchester-metropolitan-university-into-uk/IID-UK-01229/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/manchester-metropolitan-university-into-uk/IID-UK-01229/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/laurentian-university/IID-CA-00645/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/laurentian-university/IID-CA-00645/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-south-wales-qa-higher-education/IID-UK-01411/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-south-wales-qa-higher-education/IID-UK-01411/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/queens-university/IID-CA-00744/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/queens-university/IID-CA-00744/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/stevens-institute-of-technology/IID-US-00188/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/stevens-institute-of-technology/IID-US-00188/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/clark-university/IID-US-01075/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/clark-university/IID-US-01075/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/suny-new-paltz/IID-US-00049/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/suny-new-paltz/IID-US-00049/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-tasmania-melbourne-study-centre/IID-AU-01566/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-tasmania-melbourne-study-centre/IID-AU-01566/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/diablo-valley-college/IID-US-01078/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/diablo-valley-college/IID-US-01078/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-oklahoma-into-usa/IID-US-01561/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-oklahoma-into-usa/IID-US-01561/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cleveland-state-university-shorelight/IID-US-01216/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cleveland-state-university-shorelight/IID-US-01216/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/glendale-community-college-california/IID-US-00010/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/glendale-community-college-california/IID-US-00010/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/yeshiva-university/IID-US-00301/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/yeshiva-university/IID-US-00301/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-college-of-the-arts/IID-US-00971/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-college-of-the-arts/IID-US-00971/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northeast-lakeview-college-alamo-colleges/IID-US-00316/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northeast-lakeview-college-alamo-colleges/IID-US-00316/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-tasmania-international-pathway-college/IID-AU-01358/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-tasmania-international-pathway-college/IID-AU-01358/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/mcgill-university-continuing-education/IID-CA-00734/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/mcgill-university-continuing-education/IID-CA-00734/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/bradley-university/IID-US-01480/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/bradley-university/IID-US-01480/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-illinois-at-springfield/IID-US-00983/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-illinois-at-springfield/IID-US-00983/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/fashion-institute-of-design-and-merchandising/IID-US-01530/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/fashion-institute-of-design-and-merchandising/IID-US-01530/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/suffolk-university/IID-US-00953/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/suffolk-university/IID-US-00953/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/pennsylvania-state-university-dickinson-law/IID-US-01408/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/pennsylvania-state-university-dickinson-law/IID-US-01408/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/crown-institute-of-higher-education-cihe/IID-AU-01590/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/crown-institute-of-higher-education-cihe/IID-AU-01590/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/william-paterson-university-eag/IID-US-01562/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/william-paterson-university-eag/IID-US-01562/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/union-institute-of-language/IID-AU-00613/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/union-institute-of-language/IID-AU-00613/
    ] http_request                   response_time_ms=7.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-connecticut-kaplan-international/IID-US-01333/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-connecticut-kaplan-international/IID-US-01333/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-california-berkeley/IID-US-00265/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-california-berkeley/IID-US-00265/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-bridge/IID-US-01424/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-bridge/IID-US-01424/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/hult-international-business-school/IID-UK-01453/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/hult-international-business-school/IID-UK-01453/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/langports-english-language-college/IID-AU-00618/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/langports-english-language-college/IID-AU-00618/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-surrey-isc-study-group-uk/IID-UK-01369/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-surrey-isc-study-group-uk/IID-UK-01369/
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/canadore-college/IID-CA-00716/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/canadore-college/IID-CA-00716/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/south-east-technological-university-setu/IID-IE-01252/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/south-east-technological-university-setu/IID-IE-01252/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-north-texas/IID-US-00101/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-north-texas/IID-US-00101/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/ozford-college-of-business/IID-AU-00615/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/ozford-college-of-business/IID-AU-00615/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/auckland-institute-of-studies-new-zealand/IID-NZ-00901/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/auckland-institute-of-studies-new-zealand/IID-NZ-00901/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/nelson-marlborough-institute-of-technology/IID-NZ-00832/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/nelson-marlborough-institute-of-technology/IID-NZ-00832/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/australia-institute-of-business-technology/IID-AU-01385/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/australia-institute-of-business-technology/IID-AU-01385/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/florida-atlantic-university-studygroup-usa/IID-US-01394/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/florida-atlantic-university-studygroup-usa/IID-US-01394/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-birmingham-dubai/IID-UK-03169/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-birmingham-dubai/IID-UK-03169/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/builders-academy-australia/IID-AU-01397/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/builders-academy-australia/IID-AU-01397/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/manukau-institute-of-technology/IID-NZ-00831/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/manukau-institute-of-technology/IID-NZ-00831/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/florida-international-university-shorelight/IID-US-00351/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/florida-international-university-shorelight/IID-US-00351/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/ironwood-institute/IID-AU-01388/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/ironwood-institute/IID-AU-01388/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/leeds-arts-university/IID-UK-02515/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/leeds-arts-university/IID-UK-02515/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kings-education-united-states/IID-US-00341/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kings-education-united-states/IID-US-00341/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/arizona-state-university-kaplan-international/IID-US-01123/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/arizona-state-university-kaplan-international/IID-US-01123/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/southern-methodist-university/IID-US-00195/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/southern-methodist-university/IID-US-00195/
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/rowan-university/IID-US-03621/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/rowan-university/IID-US-03621/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/illinois-state-university/IID-US-00151/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/illinois-state-university/IID-US-00151/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-sheffield-international-college-study-group-uk/IID-UK-01378/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-sheffield-international-college-study-group-uk/IID-UK-01378/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/quinnipiac-university/IID-US-01398/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/quinnipiac-university/IID-US-01398/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/georgia-institute-of-technology/IID-US-00126/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/georgia-institute-of-technology/IID-US-00126/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/massey-university-college/IID-NZ-01459/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/massey-university-college/IID-NZ-01459/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/central-melbourne-institute/IID-AU-01515/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/central-melbourne-institute/IID-AU-01515/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/long-island-university-brooklyn-studygroup/IID-US-01193/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/long-island-university-brooklyn-studygroup/IID-US-01193/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/saskatchewan-colleges/IID-CA-03861/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/saskatchewan-colleges/IID-CA-03861/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/new-england-college-into/IID-US-03655/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/new-england-college-into/IID-US-03655/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-tampa/IID-US-00060/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-tampa/IID-US-00060/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/manchester-into-uk/IID-UK-01247/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/manchester-into-uk/IID-UK-01247/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/western-sydney-university/IID-AU-00520/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/western-sydney-university/IID-AU-00520/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-state-university-fullerton/IID-US-00947/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-state-university-fullerton/IID-US-00947/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/western-sydney-university/IID-AU-00520/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/western-sydney-university/IID-AU-00520/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-state-university-fullerton/IID-US-00947/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-state-university-fullerton/IID-US-00947/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/texas-state-university/IID-US-00036/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/texas-state-university/IID-US-00036/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/full-sail-university/IID-US-01206/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/full-sail-university/IID-US-01206/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cardiff-university-isc-study-group-uk/IID-UK-01364/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cardiff-university-isc-study-group-uk/IID-UK-01364/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/fairleigh-dickinson-university-canada/IID-CA-00866/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/fairleigh-dickinson-university-canada/IID-CA-00866/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/royal-college-of-art/IID-UK-01607/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/royal-college-of-art/IID-UK-01607/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/leeds-trinity-university/IID-UK-02666/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/leeds-trinity-university/IID-UK-02666/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/temple-university/IID-US-00212/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/temple-university/IID-US-00212/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-notre-dame/IID-US-00288/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-notre-dame/IID-US-00288/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/seton-hall-university/IID-US-00258/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/seton-hall-university/IID-US-00258/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/queensland-university-of-technology/IID-AU-00431/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/queensland-university-of-technology/IID-AU-00431/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/yoobee-colleges/IID-NZ-00910/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/yoobee-colleges/IID-NZ-00910/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-worcester/IID-UK-01454/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-worcester/IID-UK-01454/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/international-college-of-manitoba-navitas-at-university-of-manitoba/IID-CA-00740/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/international-college-of-manitoba-navitas-at-university-of-manitoba/IID-CA-00740/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/de-anza-college/IID-US-00311/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/de-anza-college/IID-US-00311/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-dundee/IID-UK-00795/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-dundee/IID-UK-00795/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/vancouver-film-school/IID-CA-01066/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/vancouver-film-school/IID-CA-01066/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/la-trobe-university-sydney-campus/IID-AU-00360/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/la-trobe-university-sydney-campus/IID-AU-00360/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/seattle-university/IID-US-01422/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/seattle-university/IID-US-01422/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/george-brown-college/IID-CA-00727/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/george-brown-college/IID-CA-00727/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/niagara-college/IID-CA-00741/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/niagara-college/IID-CA-00741/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/brookdale-community-college/IID-US-03929/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/brookdale-community-college/IID-US-03929/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-glasgow/IID-UK-00676/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-glasgow/IID-UK-00676/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/brookdale-community-college/IID-US-03929/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/brookdale-community-college/IID-US-03929/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-glasgow/IID-UK-00676/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-glasgow/IID-UK-00676/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/vancouver-community-college/IID-CA-01064/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/vancouver-community-college/IID-CA-01064/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/international-college-robert-gordon-university-navitas-uk/IID-UK-01254/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/international-college-robert-gordon-university-navitas-uk/IID-UK-01254/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] progress                       done=400 pct=52.1% scraper=IDPUniversityScraper total=768
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-winnipeg/IID-CA-00641/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-winnipeg/IID-CA-00641/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sibn-college/IID-AU-01539/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sibn-college/IID-AU-01539/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/st-clair-college/IID-CA-01010/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/st-clair-college/IID-CA-01010/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-regina/IID-CA-00762/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-regina/IID-CA-00762/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/tafe-nsw-institutes/IID-AU-00489/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/tafe-nsw-institutes/IID-AU-00489/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northern-lights-college/IID-CA-01056/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northern-lights-college/IID-CA-01056/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-washington/IID-US-00139/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-washington/IID-US-00139/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-at-buffalo-suny/IID-US-02501/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-at-buffalo-suny/IID-US-02501/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/niagara-college/IID-CA-00741/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/niagara-college/IID-CA-00741/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/brookdale-community-college/IID-US-03929/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/brookdale-community-college/IID-US-03929/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/william-angliss-institute-of-tafe/IID-AU-00549/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/william-angliss-institute-of-tafe/IID-AU-00549/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/saint-louis-university-globally-recruit/IID-US-00219/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/saint-louis-university-globally-recruit/IID-US-00219/
    ] http_request                   response_time_ms=5.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-glasgow/IID-UK-00676/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-glasgow/IID-UK-00676/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/vancouver-community-college/IID-CA-01064/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/vancouver-community-college/IID-CA-01064/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/green-river-college/IID-US-00013/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/green-river-college/IID-US-00013/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/international-college-robert-gordon-university-navitas-uk/IID-UK-01254/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/international-college-robert-gordon-university-navitas-uk/IID-UK-01254/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-winnipeg/IID-CA-00641/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-winnipeg/IID-CA-00641/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sibn-college/IID-AU-01539/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sibn-college/IID-AU-01539/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/st-clair-college/IID-CA-01010/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/st-clair-college/IID-CA-01010/
    ] http_request                   response_time_ms=7.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-regina/IID-CA-00762/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-regina/IID-CA-00762/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/saint-louis-university-globally-recruit/IID-US-00219/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/saint-louis-university-globally-recruit/IID-US-00219/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sunway-university/IID-MY-03487/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sunway-university/IID-MY-03487/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/florida-international-university/IID-US-00191/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/florida-international-university/IID-US-00191/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/troy-university/IID-US-00050/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/troy-university/IID-US-00050/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-kentucky/IID-US-00276/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-kentucky/IID-US-00276/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-rochester/IID-US-00290/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-rochester/IID-US-00290/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/deakin-university/IID-AU-00402/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/deakin-university/IID-AU-00402/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/london-metropolitan-university/IID-UK-01350/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/london-metropolitan-university/IID-UK-01350/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/architectural-association-school-of-architecture/IID-UK-04066/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/architectural-association-school-of-architecture/IID-UK-04066/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/jmc-academy/IID-AU-00601/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/jmc-academy/IID-AU-00601/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/george-mason-university-into-usa/IID-US-01182/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/george-mason-university-into-usa/IID-US-01182/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/pittsburg-state-university/IID-US-01185/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/pittsburg-state-university/IID-US-01185/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/william-angliss-institute-of-tafe/IID-AU-00549/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/william-angliss-institute-of-tafe/IID-AU-00549/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/south-seattle-college/IID-US-00002/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/south-seattle-college/IID-US-00002/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/aston-university-birmingham/IID-UK-00661/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/aston-university-birmingham/IID-UK-00661/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/green-river-college/IID-US-00013/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/green-river-college/IID-US-00013/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/seneca-polytechnic/IID-CA-00652/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/seneca-polytechnic/IID-CA-00652/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/james-cook-university/IID-AU-00409/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/james-cook-university/IID-AU-00409/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/melbourne-institute-of-technology-mit/IID-AU-00553/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/melbourne-institute-of-technology-mit/IID-AU-00553/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/arizona-state-university-kaplan-international/IID-US-01123/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/arizona-state-university-kaplan-international/IID-US-01123/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/north-seattle-college/IID-US-00003/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/north-seattle-college/IID-US-00003/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-michener-institute-for-applied-health-science/IID-CA-00750/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-michener-institute-for-applied-health-science/IID-CA-00750/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/columbia-college/IID-CA-00720/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/columbia-college/IID-CA-00720/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/new-york-institute-of-technology-vancouver/IID-CA-01097/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/new-york-institute-of-technology-vancouver/IID-CA-01097/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/georgian-college-at-ilac/IID-CA-01345/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/georgian-college-at-ilac/IID-CA-01345/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/crandall-university/IID-CA-01177/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/crandall-university/IID-CA-01177/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kings-university-college-at-western-university/IID-CA-00849/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kings-university-college-at-western-university/IID-CA-00849/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/catc-design-school/IID-AU-00617/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/catc-design-school/IID-AU-00617/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/academy-of-interactive-entertainment/IID-AU-00602/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/academy-of-interactive-entertainment/IID-AU-00602/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/unisc-adelaide/IID-AU-03235/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/unisc-adelaide/IID-AU-03235/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/queensland-college-of-art/IID-AU-00437/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/queensland-college-of-art/IID-AU-00437/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/institute-of-health-management/IID-AU-01342/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/institute-of-health-management/IID-AU-01342/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/guildhouse-school-cats-london/IID-UK-01155/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/guildhouse-school-cats-london/IID-UK-01155/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/up-international-college-aut/IID-NZ-01381/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/up-international-college-aut/IID-NZ-01381/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/oncampus-sunderland/IID-UK-01161/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/oncampus-sunderland/IID-UK-01161/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/up-international-college-victoria-university-of-wellington/IID-NZ-01380/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/up-international-college-victoria-university-of-wellington/IID-NZ-01380/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/magill-college-sydney/IID-AU-00577/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/magill-college-sydney/IID-AU-00577/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/allied-institute/IID-AU-02832/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/allied-institute/IID-AU-02832/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/gordon-institute-of-tafe/IID-AU-00372/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/gordon-institute-of-tafe/IID-AU-00372/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-texas-san-antonio/IID-US-00955/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-texas-san-antonio/IID-US-00955/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/suny-stony-brook-university/IID-US-00177/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/suny-stony-brook-university/IID-US-00177/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/miracosta-college/IID-US-01269/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/miracosta-college/IID-US-01269/
    ] http_request                   response_time_ms=8.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sae-usa/IID-US-00324/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sae-usa/IID-US-00324/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/new-york-film-academy/IID-US-01183/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/new-york-film-academy/IID-US-01183/
    ] http_request                   response_time_ms=10.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-california-irvine-extension-irvine-division-of-continuing-education/IID-US-01528/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-california-irvine-extension-irvine-division-of-continuing-education/IID-US-01528/
    ] http_request                   response_time_ms=8.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/higher-education-leadership-institute-heli/IID-AU-01565/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/higher-education-leadership-institute-heli/IID-AU-01565/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/college-of-southern-nevada/IID-US-01017/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/college-of-southern-nevada/IID-US-01017/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/southern-arkansas-university-main-campus/IID-US-00992/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/southern-arkansas-university-main-campus/IID-US-00992/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/worcester-state-university/IID-US-01210/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/worcester-state-university/IID-US-01210/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/massachusetts-institute-of-technology/IID-US-00090/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/massachusetts-institute-of-technology/IID-US-00090/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/australian-maritime-college/IID-AU-00484/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/australian-maritime-college/IID-AU-00484/
    ] http_request                   response_time_ms=8.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/michigan-technological-university/IID-US-00243/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/michigan-technological-university/IID-US-00243/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-manchester-into-uk/IID-UK-01234/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-manchester-into-uk/IID-UK-01234/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/oxford-international-halifax/IID-CA-00887/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/oxford-international-halifax/IID-CA-00887/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-maine/IID-US-00278/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-maine/IID-US-00278/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/academies-australasia-polytechnic-pty-limited/IID-AU-00605/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/academies-australasia-polytechnic-pty-limited/IID-AU-00605/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/deakin-uni-lancaster-uni-indonesia-dli/IID-AU-03334/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/deakin-uni-lancaster-uni-indonesia-dli/IID-AU-03334/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/rochester-institute-of-technology/IID-US-00991/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/rochester-institute-of-technology/IID-US-00991/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/pepperdine-university/IID-US-00255/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/pepperdine-university/IID-US-00255/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-college-dublin/IID-IE-01119/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-college-dublin/IID-IE-01119/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-central-florida/IID-US-00211/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-central-florida/IID-US-00211/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/tamwood-canada/IID-CA-01522/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/tamwood-canada/IID-CA-01522/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-north-florida/IID-US-00974/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-north-florida/IID-US-00974/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-oxford/IID-UK-01026/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-oxford/IID-UK-01026/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/leeds-beckett-isc-study-group-uk/IID-UK-01371/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/leeds-beckett-isc-study-group-uk/IID-UK-01371/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/ara-institute-of-canterbury-limited/IID-NZ-00829/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/ara-institute-of-canterbury-limited/IID-NZ-00829/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/alliance-college/IID-AU-01328/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/alliance-college/IID-AU-01328/
    ] http_request                   response_time_ms=7.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/fleming-college-toronto/IID-CA-01409/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/fleming-college-toronto/IID-CA-01409/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/shafston-international-college/IID-AU-00552/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/shafston-international-college/IID-AU-00552/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/carleton-university/IID-CA-00718/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/carleton-university/IID-CA-00718/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-state-university-northridge/IID-US-00949/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-state-university-northridge/IID-US-00949/
    ] http_request                   response_time_ms=8.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-state-university-san-bernardino/IID-US-01041/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-state-university-san-bernardino/IID-US-01041/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/ec-english-language-centres-canada/IID-CA-00915/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/ec-english-language-centres-canada/IID-CA-00915/
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/whitecliffe/IID-NZ-01284/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/whitecliffe/IID-NZ-01284/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/brock-university/IID-CA-00653/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/brock-university/IID-CA-00653/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/eastern-washington-university/IID-US-02523/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/eastern-washington-university/IID-US-02523/
    ] http_request                   response_time_ms=10.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-limerick/IID-IE-01151/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-limerick/IID-IE-01151/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/tafe-south-australia/IID-AU-00376/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/tafe-south-australia/IID-AU-00376/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/oregon-state-university-into-usa/IID-US-01179/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/oregon-state-university-into-usa/IID-US-01179/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/oncampus-london-south-bank/IID-UK-01160/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/oncampus-london-south-bank/IID-UK-01160/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] progress                       done=500 pct=65.1% scraper=IDPUniversityScraper total=768
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-tulsa/IID-US-00293/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-tulsa/IID-US-00293/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/san-diego-state-university/IID-US-00951/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/san-diego-state-university/IID-US-00951/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-minnesota-twin-cities/IID-US-00282/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-minnesota-twin-cities/IID-US-00282/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-oklahoma/IID-US-00289/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-oklahoma/IID-US-00289/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/james-cook-university-singapore-campus/IID-AU-01400/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/james-cook-university-singapore-campus/IID-AU-01400/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-tulsa/IID-US-00293/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-tulsa/IID-US-00293/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/san-diego-state-university/IID-US-00951/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/san-diego-state-university/IID-US-00951/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-minnesota-twin-cities/IID-US-00282/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-minnesota-twin-cities/IID-US-00282/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-oklahoma/IID-US-00289/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-oklahoma/IID-US-00289/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/royal-holloway-university-of-london-isc-study-group-uk/IID-UK-01370/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/royal-holloway-university-of-london-isc-study-group-uk/IID-UK-01370/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/oncampus-amsterdam/IID-UK-03001/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/oncampus-amsterdam/IID-UK-03001/
    ] http_request                   response_time_ms=9.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-north-carolina-at-chapel-hill/IID-US-00286/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-north-carolina-at-chapel-hill/IID-US-00286/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/western-institute-of-technology/IID-NZ-01225/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/western-institute-of-technology/IID-NZ-01225/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/worcester-polytechnic-institute/IID-US-00124/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/worcester-polytechnic-institute/IID-US-00124/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-buckingham/IID-UK-00660/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-buckingham/IID-UK-00660/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-stirling/IID-UK-00701/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-stirling/IID-UK-00701/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/california-state-university-long-beach/IID-US-00948/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/california-state-university-long-beach/IID-US-00948/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/academia-international/IID-AU-00619/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/academia-international/IID-AU-00619/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/tennessee-technological-university/IID-US-00978/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/tennessee-technological-university/IID-US-00978/
    ] http_request                   response_time_ms=8.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/wake-forest-university/IID-US-00213/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/wake-forest-university/IID-US-00213/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-pennsylvania/IID-US-00097/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-pennsylvania/IID-US-00097/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/st-phillips-college-alamo-colleges/IID-US-00314/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/st-phillips-college-alamo-colleges/IID-US-00314/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/drew-university-into-usa/IID-US-01167/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/drew-university-into-usa/IID-US-01167/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-miami/IID-US-00203/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-miami/IID-US-00203/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-san-francisco/IID-US-00143/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-san-francisco/IID-US-00143/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/michigan-state-university/IID-US-00113/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/michigan-state-university/IID-US-00113/
    ] http_request                   response_time_ms=8.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-huddersfield-london-study-group-uk/IID-UK-01373/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-huddersfield-london-study-group-uk/IID-UK-01373/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/toronto-metropolitan-university-international-college/IID-CA-01319/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/toronto-metropolitan-university-international-college/IID-CA-01319/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/centennial-college-of-applied-arts-and-technology/IID-CA-00719/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/centennial-college-of-applied-arts-and-technology/IID-CA-00719/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/johnson-and-wales-university/IID-US-00930/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/johnson-and-wales-university/IID-US-00930/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-victoria-kaplan/IID-CA-01544/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-victoria-kaplan/IID-CA-01544/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-east-anglia-uea/IID-UK-00704/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-east-anglia-uea/IID-UK-00704/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-victoria/IID-CA-00765/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-victoria/IID-CA-00765/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/college-of-the-rockies/IID-CA-01061/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/college-of-the-rockies/IID-CA-01061/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/griffith-college-australia/IID-AU-00563/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/griffith-college-australia/IID-AU-00563/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/wilfrid-laurier-university/IID-CA-00647/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/wilfrid-laurier-university/IID-CA-00647/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/oxford-international-education-group-north-america/IID-CA-02869/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/oxford-international-education-group-north-america/IID-CA-02869/
    ] http_request                   response_time_ms=5.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/education-centre-of-australia-eca/IID-AU-01172/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/education-centre-of-australia-eca/IID-AU-01172/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lead-college-pty-ltd/IID-AU-01456/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lead-college-pty-ltd/IID-AU-01456/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/swinburne-university-of-technology-vietnam-campus/IID-AU-01355/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/swinburne-university-of-technology-vietnam-campus/IID-AU-01355/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/coast-mountain-college/IID-CA-01058/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/coast-mountain-college/IID-CA-01058/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-guelph/IID-CA-00757/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-guelph/IID-CA-00757/
    ] http_request                   response_time_ms=8.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lakehead-university/IID-CA-00732/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lakehead-university/IID-CA-00732/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-virginia/IID-US-00156/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-virginia/IID-US-00156/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/western-university/IID-CA-00766/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/western-university/IID-CA-00766/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/berkeley-college/IID-US-01173/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/berkeley-college/IID-US-01173/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cambridge-school-of-visual-and-performing-arts/IID-UK-01152/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cambridge-school-of-visual-and-performing-arts/IID-UK-01152/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/swansea-university/IID-UK-00666/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/swansea-university/IID-UK-00666/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/douglas-college/IID-CA-00993/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/douglas-college/IID-CA-00993/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/norquest-college/IID-CA-01112/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/norquest-college/IID-CA-01112/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/birkbeck-university-of-london/IID-UK-00800/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/birkbeck-university-of-london/IID-UK-00800/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/rcsi-ucd-malaysia-campus/IID-MY-03485/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/rcsi-ucd-malaysia-campus/IID-MY-03485/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/rcsi-ucd-malaysia-campus/IID-MY-03485/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/rcsi-ucd-malaysia-campus/IID-MY-03485/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/london-business-school-university-of-london/IID-UK-04032/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/london-business-school-university-of-london/IID-UK-04032/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/help-university/IID-MY-03481/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/help-university/IID-MY-03481/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/baruch-college-cuny/IID-US-00988/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/baruch-college-cuny/IID-US-00988/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/massachusetts-college-of-pharmacy-and-health-sciences/IID-US-00962/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/massachusetts-college-of-pharmacy-and-health-sciences/IID-US-00962/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kwantlen-polytechnic-university/IID-CA-00731/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kwantlen-polytechnic-university/IID-CA-00731/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northern-college/IID-CA-01043/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northern-college/IID-CA-01043/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/durham-university/IID-UK-00699/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/durham-university/IID-UK-00699/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-tennessee-knoxville/IID-US-00225/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-tennessee-knoxville/IID-US-00225/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-queensland/IID-AU-00379/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-queensland/IID-AU-00379/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-newcastle/IID-AU-00400/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-newcastle/IID-AU-00400/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/james-cook-university-singapore-campus/IID-AU-01400/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/james-cook-university-singapore-campus/IID-AU-01400/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/box-hill-institute/IID-AU-00371/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/box-hill-institute/IID-AU-00371/
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-new-orleans/IID-US-00136/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-new-orleans/IID-US-00136/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/gannon-university/IID-US-00963/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/gannon-university/IID-US-00963/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-denver/IID-US-00271/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-denver/IID-US-00271/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kent-state-university/IID-US-00064/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kent-state-university/IID-US-00064/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-connecticut/IID-US-00196/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-connecticut/IID-US-00196/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/technological-university-of-the-shannon-midlands-midwest/IID-IE-01244/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/technological-university-of-the-shannon-midlands-midwest/IID-IE-01244/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/monash-university/IID-AU-00369/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/monash-university/IID-AU-00369/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-georgia/IID-US-00273/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-georgia/IID-US-00273/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-leeds/IID-UK-00782/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-leeds/IID-UK-00782/
    ] http_request                   response_time_ms=7.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/monash-university-malaysia/IID-AU-00363/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/monash-university-malaysia/IID-AU-00363/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/de-montfort-university/IID-UK-00705/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/de-montfort-university/IID-UK-00705/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-melbourne/IID-AU-00408/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-melbourne/IID-AU-00408/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/engineering-institute-of-technology/IID-AU-01318/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/engineering-institute-of-technology/IID-AU-01318/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/de-montfort-university/IID-UK-00705/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/de-montfort-university/IID-UK-00705/
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/city-st-georges-university-of-london/IID-UK-00847/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/city-st-georges-university-of-london/IID-UK-00847/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=5.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sheridan-college-institute-of-technology-and-advanced-learning/IID-CA-00748/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sheridan-college-institute-of-technology-and-advanced-learning/IID-CA-00748/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/nottingham-trent-university/IID-UK-01040/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/nottingham-trent-university/IID-UK-01040/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/soas-university-of-london/IID-UK-01042/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/soas-university-of-london/IID-UK-01042/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-queensland/IID-AU-00379/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-queensland/IID-AU-00379/
    ] http_request                   response_time_ms=7.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/dawson-college/IID-CA-01103/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/dawson-college/IID-CA-01103/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northern-college-at-pures-toronto/IID-CA-01336/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northern-college-at-pures-toronto/IID-CA-01336/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northwestern-polytechnic/IID-CA-01402/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northwestern-polytechnic/IID-CA-01402/
    ] http_request                   response_time_ms=8.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/centre-for-english-language-teaching-the-university-of-western-australia/IID-AU-00418/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/centre-for-english-language-teaching-the-university-of-western-australia/IID-AU-00418/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/rochester-independent-college-dukes-education/IID-UK-03202/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/rochester-independent-college-dukes-education/IID-UK-03202/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/trebas-institute/IID-CA-01340/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/trebas-institute/IID-CA-01340/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-brighton-international-college-kaplan-uk/IID-UK-01303/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-brighton-international-college-kaplan-uk/IID-UK-01303/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-alabama/IID-US-00185/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-alabama/IID-US-00185/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/concordia-university/IID-CA-00721/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/concordia-university/IID-CA-00721/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/russo-business-school/IID-AU-01016/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/russo-business-school/IID-AU-01016/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/australian-wings-academy/IID-AU-00533/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/australian-wings-academy/IID-AU-00533/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/billy-blue-college-of-design/IID-AU-00441/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/billy-blue-college-of-design/IID-AU-00441/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/collarts/IID-AU-01240/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/collarts/IID-AU-01240/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/australia-international-institute-of-workplace-training/IID-AU-00622/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/australia-international-institute-of-workplace-training/IID-AU-00622/
    ] http_request                   response_time_ms=8.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/bournemouth-university-international-college-kaplan-uk/IID-UK-01297/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/bournemouth-university-international-college-kaplan-uk/IID-UK-01297/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kings-own-institute/IID-AU-00995/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kings-own-institute/IID-AU-00995/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] progress                       done=600 pct=78.1% scraper=IDPUniversityScraper total=768
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/everthought-college-of-construction/IID-AU-01176/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/everthought-college-of-construction/IID-AU-01176/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/missouri-university-of-science-and-technology/IID-US-00187/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/missouri-university-of-science-and-technology/IID-US-00187/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-texas-el-paso/IID-US-00112/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-texas-el-paso/IID-US-00112/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-california-riverside-engineering/IID-US-01588/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-california-riverside-engineering/IID-US-01588/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/holland-college/IID-CA-01109/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/holland-college/IID-CA-01109/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-toronto/IID-CA-00764/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-toronto/IID-CA-00764/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/louisiana-state-university-shorelight/IID-US-00937/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/louisiana-state-university-shorelight/IID-US-00937/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/santa-barbara-city-college/IID-US-00018/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/santa-barbara-city-college/IID-US-00018/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/maryland-institute-college-of-art/IID-US-00067/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/maryland-institute-college-of-art/IID-US-00067/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/huron-university-college/IID-CA-01608/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/huron-university-college/IID-CA-01608/
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/ucl-centre-for-languages-and-international-education-clie/IID-UK-01431/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/ucl-centre-for-languages-and-international-education-clie/IID-UK-01431/
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/skyline-college/IID-US-01273/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/skyline-college/IID-US-01273/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/holmes-education-group-ireland/IID-IE-01537/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/holmes-education-group-ireland/IID-IE-01537/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/munster-technological-university/IID-IE-01527/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/munster-technological-university/IID-IE-01527/
    ] http_request                   response_time_ms=9.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/royal-college-of-surgeons-in-ireland/IID-IE-01122/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/royal-college-of-surgeons-in-ireland/IID-IE-01122/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/saginaw-valley-state-university/IID-US-00051/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/saginaw-valley-state-university/IID-US-00051/
    ] http_request                   response_time_ms=8.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-kansas-shorelight/IID-US-00350/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-kansas-shorelight/IID-US-00350/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-chicago/IID-US-00214/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-chicago/IID-US-00214/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/contra-costa-college/IID-US-01077/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/contra-costa-college/IID-US-01077/
    ] http_request                   response_time_ms=9.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/auburn-university-at-montgomery-shorelight/IID-US-01067/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/auburn-university-at-montgomery-shorelight/IID-US-01067/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=8.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/mt-san-antonio-college/IID-US-01271/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/mt-san-antonio-college/IID-US-01271/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lancaster-university-into-uk/IID-UK-01551/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lancaster-university-into-uk/IID-UK-01551/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/canadian-college-of-english-language/IID-CA-00889/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/canadian-college-of-english-language/IID-CA-00889/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/bucksmore-education/IID-UK-01508/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/bucksmore-education/IID-UK-01508/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/dublin-business-school/IID-IE-01136/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/dublin-business-school/IID-IE-01136/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/basair-aviation-college/IID-AU-00554/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/basair-aviation-college/IID-AU-00554/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/malvern-international-plc/IID-UK-01451/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/malvern-international-plc/IID-UK-01451/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cambrian-college/IID-CA-00715/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cambrian-college/IID-CA-00715/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-massachusetts-amherst-into-usa/IID-US-01423/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-massachusetts-amherst-into-usa/IID-US-01423/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-massachusetts-amherst/IID-US-00142/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-massachusetts-amherst/IID-US-00142/
    ] http_request                   response_time_ms=7.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/hult-international-business-school/IID-US-00322/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/hult-international-business-school/IID-US-00322/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/harvard-university/IID-US-00065/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/harvard-university/IID-US-00065/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-aberdeen-isc-study-group-uk/IID-UK-01372/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-aberdeen-isc-study-group-uk/IID-UK-01372/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/greystone-college/IID-CA-01029/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/greystone-college/IID-CA-01029/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-birmingham-foundation-pathways-kaplan-uk/IID-UK-01414/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-birmingham-foundation-pathways-kaplan-uk/IID-UK-01414/
    ] http_request                   response_time_ms=5.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northern-arizona-university/IID-US-00037/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northern-arizona-university/IID-US-00037/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-california-irvine/IID-US-00267/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-california-irvine/IID-US-00267/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/queensland-international-business-academy/IID-AU-00550/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/queensland-international-business-academy/IID-AU-00550/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/imagine-education-australia/IID-AU-00625/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/imagine-education-australia/IID-AU-00625/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/otago-polytechnic/IID-NZ-00914/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/otago-polytechnic/IID-NZ-00914/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/adelaide-education-group/IID-AU-01360/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/adelaide-education-group/IID-AU-01360/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/thomas-jefferson-university-into-usa/IID-US-01348/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/thomas-jefferson-university-into-usa/IID-US-01348/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-the-pacific/IID-US-03622/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-the-pacific/IID-US-03622/
    ] http_request                   response_time_ms=7.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sero-institute/IID-AU-01405/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sero-institute/IID-AU-01405/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/pacific-international-hotel-management-school-limited/IID-NZ-01462/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/pacific-international-hotel-management-school-limited/IID-NZ-01462/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/australian-language-schools-pty-ltd/IID-AU-00627/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/australian-language-schools-pty-ltd/IID-AU-00627/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/st-johns-university/IID-US-00181/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/st-johns-university/IID-US-00181/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/new-york-institute-of-technology/IID-US-00979/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/new-york-institute-of-technology/IID-US-00979/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/centre-for-english-teaching-the-university-of-sydney/IID-AU-00526/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/centre-for-english-teaching-the-university-of-sydney/IID-AU-00526/
    ] http_request                   response_time_ms=14.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kaplan-university-of-alberta/IID-CA-02500/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kaplan-university-of-alberta/IID-CA-02500/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-california-los-angeles/IID-US-00199/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-california-los-angeles/IID-US-00199/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/oncampus-ireland/IID-IE-01564/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/oncampus-ireland/IID-IE-01564/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/texas-a-and-m-university-college-station/IID-US-00116/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/texas-a-and-m-university-college-station/IID-US-00116/
    ] http_request                   response_time_ms=8.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/ball-state-university/IID-US-00154/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/ball-state-university/IID-US-00154/
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/media-design-school/IID-NZ-01287/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/media-design-school/IID-NZ-01287/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-exeter-into-uk/IID-UK-01227/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-exeter-into-uk/IID-UK-01227/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/australian-college-of-applied-professionals/IID-AU-00536/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/australian-college-of-applied-professionals/IID-AU-00536/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-galway/IID-IE-01120/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-galway/IID-IE-01120/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-northampton/IID-UK-01437/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-northampton/IID-UK-01437/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-ottawa/IID-CA-00761/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-ottawa/IID-CA-00761/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/colorado-state-university/IID-US-00069/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/colorado-state-university/IID-US-00069/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-east-anglia-into-uk/IID-UK-01226/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-east-anglia-into-uk/IID-UK-01226/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/fordham-university/IID-US-00235/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/fordham-university/IID-US-00235/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/uwa-college/IID-AU-01396/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/uwa-college/IID-AU-01396/
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/school-of-the-art-institute-of-chicago/IID-US-00961/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/school-of-the-art-institute-of-chicago/IID-US-00961/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/southern-illinois-university-carbondale-into/IID-US-03754/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/southern-illinois-university-carbondale-into/IID-US-03754/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/national-university/IID-US-00045/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/national-university/IID-US-00045/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cardiff-metropolitan-university/IID-UK-00678/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cardiff-metropolitan-university/IID-UK-00678/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/cranfield-university/IID-UK-00804/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/cranfield-university/IID-UK-00804/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northwestern-university/IID-US-00250/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northwestern-university/IID-US-00250/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-staffordshire/IID-UK-00846/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-staffordshire/IID-UK-00846/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/oakland-university/IID-US-00251/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/oakland-university/IID-US-00251/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-surrey/IID-UK-00673/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-surrey/IID-UK-00673/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/edith-cowan-college/IID-AU-00535/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/edith-cowan-college/IID-AU-00535/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/curtin-college/IID-AU-00588/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/curtin-college/IID-AU-00588/
    ] http_request                   response_time_ms=5.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/western-sydney-university-sydney-city-campus/IID-AU-01003/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/western-sydney-university-sydney-city-campus/IID-AU-01003/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-suffolk/IID-UK-01526/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-suffolk/IID-UK-01526/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-guelph-humber/IID-CA-01059/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-guelph-humber/IID-CA-01059/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/st-marys-university-twickenham/IID-UK-01439/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/st-marys-university-twickenham/IID-UK-01439/
    ] http_request                   response_time_ms=8.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/wrexham-university/IID-UK-01447/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/wrexham-university/IID-UK-01447/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/loyalist-college-of-applied-arts-and-technology/IID-CA-00695/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/loyalist-college-of-applied-arts-and-technology/IID-CA-00695/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/la-trobe-college-australia/IID-AU-00407/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/la-trobe-college-australia/IID-AU-00407/
    ] http_request                   response_time_ms=7.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-roehampton/IID-UK-00786/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-roehampton/IID-UK-00786/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lasalle-college-vancouver/IID-CA-01413/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lasalle-college-vancouver/IID-CA-01413/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-roehampton/IID-UK-00786/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-roehampton/IID-UK-00786/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/lasalle-college-vancouver/IID-CA-01413/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/lasalle-college-vancouver/IID-CA-01413/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/ilac-international-college/IID-CA-01346/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/ilac-international-college/IID-CA-01346/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/trinity-western-university/IID-CA-00753/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/trinity-western-university/IID-CA-00753/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-hertfordshire/IID-UK-00784/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-hertfordshire/IID-UK-00784/
    ] http_request                   response_time_ms=7.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-birmingham/IID-UK-00780/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-birmingham/IID-UK-00780/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/london-school-of-business-and-finance-malaysia/IID-MY-03486/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/london-school-of-business-and-finance-malaysia/IID-MY-03486/
    ] http_request                   response_time_ms=7.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/asa-institute-of-higher-education/IID-AU-02902/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/asa-institute-of-higher-education/IID-AU-02902/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/santa-clara-university/IID-US-03965/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/santa-clara-university/IID-US-03965/
    ] http_request                   response_time_ms=7.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-college-birmingham/IID-UK-03998/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-college-birmingham/IID-UK-03998/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/royal-holloway-university-of-london/IID-UK-00655/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/royal-holloway-university-of-london/IID-UK-00655/
    ] http_request                   response_time_ms=8.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sheffield-hallam-university/IID-UK-00690/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sheffield-hallam-university/IID-UK-00690/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/royal-holloway-university-of-london/IID-UK-00655/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/royal-holloway-university-of-london/IID-UK-00655/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sheffield-hallam-university/IID-UK-00690/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sheffield-hallam-university/IID-UK-00690/
    ] http_request                   response_time_ms=8.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/capilano-university/IID-CA-00717/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/capilano-university/IID-CA-00717/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/dublin-city-university/IID-IE-01248/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/dublin-city-university/IID-IE-01248/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] progress                       done=700 pct=91.1% scraper=IDPUniversityScraper total=768
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/dalhousie-university/IID-CA-00644/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/dalhousie-university/IID-CA-00644/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/victorian-college-of-arts/IID-AU-00398/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/victorian-college-of-arts/IID-AU-00398/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/eastern-michigan-university/IID-US-00940/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/eastern-michigan-university/IID-US-00940/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/southern-cross-university/IID-AU-00532/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/southern-cross-university/IID-AU-00532/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/georgia-state-university/IID-US-00178/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/georgia-state-university/IID-US-00178/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/johns-hopkins-university/IID-US-00239/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/johns-hopkins-university/IID-US-00239/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/equals-international-pty-ltd/IID-AU-00999/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/equals-international-pty-ltd/IID-AU-00999/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kingston-university/IID-UK-00702/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kingston-university/IID-UK-00702/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/adelphi-university-shorelight/IID-US-00997/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/adelphi-university-shorelight/IID-US-00997/
    ] http_request                   response_time_ms=6.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-cumbria/IID-UK-01449/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-cumbria/IID-UK-01449/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/conestoga-college/IID-CA-00722/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/conestoga-college/IID-CA-00722/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-wales-trinity-saint-david/IID-UK-04065/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-wales-trinity-saint-david/IID-UK-04065/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/macquarie-university/IID-AU-00366/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/macquarie-university/IID-AU-00366/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kaplan-business-school/IID-AU-00628/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kaplan-business-school/IID-AU-00628/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-edinburgh/IID-UK-00685/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-edinburgh/IID-UK-00685/
    ] http_request                   response_time_ms=6.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/australian-pacific-college/IID-AU-00537/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/australian-pacific-college/IID-AU-00537/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/tulane-university-shorelight/IID-US-01390/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/tulane-university-shorelight/IID-US-01390/
    ] http_request                   response_time_ms=8.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/oncampus-loughborough/IID-UK-01427/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/oncampus-loughborough/IID-UK-01427/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-aberdeen/IID-UK-00794/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-aberdeen/IID-UK-00794/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/international-college-portsmouth-navitas-uk/IID-UK-01253/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/international-college-portsmouth-navitas-uk/IID-UK-01253/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/international-college-portsmouth-navitas-uk/IID-UK-01253/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/international-college-portsmouth-navitas-uk/IID-UK-01253/
    ] http_request                   response_time_ms=11.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/vanier-college/IID-CA-01105/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/vanier-college/IID-CA-01105/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/future-english/IID-AU-02833/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/future-english/IID-AU-02833/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/navitas-english-services-pty-ltd-formerly-acl/IID-AU-00381/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/navitas-english-services-pty-ltd-formerly-acl/IID-AU-00381/
    ] http_request                   response_time_ms=7.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/usq-sydney-education-centre/IID-AU-00596/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/usq-sydney-education-centre/IID-AU-00596/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-university-of-auckland-international-college/IID-NZ-01376/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-university-of-auckland-international-college/IID-NZ-01376/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/australian-national-college-of-beauty/IID-AU-00770/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/australian-national-college-of-beauty/IID-AU-00770/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-hawaii-manoa/IID-US-00274/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-hawaii-manoa/IID-US-00274/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/sunraysia-institute-of-tafe/IID-AU-00576/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/sunraysia-institute-of-tafe/IID-AU-00576/
    ] http_request                   response_time_ms=5.7 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/st-george-sutherland-community-college/IID-AU-01286/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/st-george-sutherland-community-college/IID-AU-01286/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/london-world-education-centre-into-uk/IID-UK-01236/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/london-world-education-centre-into-uk/IID-UK-01236/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/wimbledon-school-of-english/IID-UK-00860/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/wimbledon-school-of-english/IID-UK-00860/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/international-travel-college-of-nz/IID-NZ-00900/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/international-travel-college-of-nz/IID-NZ-00900/
    ] http_request                   response_time_ms=5.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/language-specialist-international/IID-UK-00857/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/language-specialist-international/IID-UK-00857/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/elite-school-of-beauty-spa/IID-NZ-01048/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/elite-school-of-beauty-spa/IID-NZ-01048/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/aspire2-international/IID-NZ-00899/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/aspire2-international/IID-NZ-00899/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/alberta-university-of-the-arts/IID-CA-02590/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/alberta-university-of-the-arts/IID-CA-02590/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/christchurch-college-of-english/IID-NZ-00897/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/christchurch-college-of-english/IID-NZ-00897/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/hilton-academy-pty-ltd/IID-AU-02834/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/hilton-academy-pty-ltd/IID-AU-02834/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/paragon-polytechnic/IID-AU-02835/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/paragon-polytechnic/IID-AU-02835/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/algonquin-college/IID-CA-00698/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/algonquin-college/IID-CA-00698/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/san-antonio-college-alamo-colleges/IID-US-00315/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/san-antonio-college-alamo-colleges/IID-US-00315/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-waterloo/IID-CA-00667/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-waterloo/IID-CA-00667/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/hanson-college-of-business-health-and-technology/IID-CA-01538/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/hanson-college-of-business-health-and-technology/IID-CA-01538/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/saint-louis-university-into-usa/IID-US-01171/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/saint-louis-university-into-usa/IID-US-01171/
    ] http_request                   response_time_ms=6.9 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/loyola-marymount-university/IID-US-00968/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/loyola-marymount-university/IID-US-00968/
    ] http_request                   response_time_ms=7.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-montana/IID-US-00283/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-montana/IID-US-00283/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/the-language-company-kirksville/IID-US-00932/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/the-language-company-kirksville/IID-US-00932/
    ] http_request                   response_time_ms=6.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-york-international-pathway-college-kaplan-uk/IID-UK-01305/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-york-international-pathway-college-kaplan-uk/IID-UK-01305/
    ] http_request                   response_time_ms=7.6 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/qut-college/IID-AU-00432/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/qut-college/IID-AU-00432/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/alexander-college/IID-CA-01201/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/alexander-college/IID-CA-01201/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/american-university-shorelight/IID-US-01000/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/american-university-shorelight/IID-US-01000/
    ] http_request                   response_time_ms=8.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/northwest-missouri-state-university/IID-US-01389/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/northwest-missouri-state-university/IID-US-01389/
    ] http_request                   response_time_ms=5.8 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kaplan-uk/IID-UK-00848/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kaplan-uk/IID-UK-00848/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/els-language-centres/IID-US-01518/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/els-language-centres/IID-US-01518/
    ] http_request                   response_time_ms=7.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/art-center-college-of-design/IID-US-00965/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/art-center-college-of-design/IID-US-00965/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/dartmouth-college/IID-US-00171/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/dartmouth-college/IID-US-00171/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/western-washington-university-international-study-center-studygroup/IID-US-01086/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/western-washington-university-international-study-center-studygroup/IID-US-01086/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/kangan-institute/IID-AU-00531/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/kangan-institute/IID-AU-00531/
    ] http_request                   response_time_ms=6.5 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/centre-of-english-studies-toronto/IID-CA-01184/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/centre-of-english-studies-toronto/IID-CA-01184/
Error:    ] batch_bulk_upsert_failed       count=20 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/victoria-university-brisbane/IID-AU-01570/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/victoria-university-brisbane/IID-AU-01570/
    ] http_request                   response_time_ms=6.1 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/alma-mater-college-australia/IID-AU-01429/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/alma-mater-college-australia/IID-AU-01429/
    ] http_request                   response_time_ms=7.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/blue-mountains-international-hotel-management-school/IID-AU-00519/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/blue-mountains-international-hotel-management-school/IID-AU-00519/
    ] http_request                   response_time_ms=6.0 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/university-of-california-davis/IID-US-00266/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/university-of-california-davis/IID-US-00266/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/yorkville-university/IID-CA-01556/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/yorkville-university/IID-CA-01556/
    ] http_request                   response_time_ms=6.4 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/purdue-university-northwest/IID-US-01200/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/purdue-university-northwest/IID-US-01200/
    ] http_request                   response_time_ms=6.3 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/maryville-university/IID-US-01211/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/maryville-university/IID-US-01211/
    ] http_request                   response_time_ms=6.2 scraper=IDPUniversityScraper status_code=403 url=https://www.idp.com/universities-and-colleges/mercer-university-studygroup/IID-US-03268/
Warning:  ] http_forbidden                 scraper=IDPUniversityScraper url=https://www.idp.com/universities-and-colleges/mercer-university-studygroup/IID-US-03268/
Error:    ] batch_bulk_upsert_failed       count=8 error="cannot import name 'bulk_upsert_universities' from 'src.database.queries' (/home/runner/work/scholarradar/scholarradar/src/database/queries.py)" scraper=IDPUniversityScraper
    ] scrape_complete                scraper=IDPUniversityScraper total=768
    ] scraper_complete               count=768 scraper=idp_universities
    ] group_complete                 counts={'scholarships': 480, 'courses': 6924, 'universities': 768} elapsed_seconds=245.3 group=heavy
    ] group_start                    group=fast scrapers=['visa', 'cost', 'govt', 'phd']
    ] scraping_visa_page             country=australia scraper=IDPVisaScraper url=https://www.idp.com/nepal/blog/latest-visa-news/
    ] scraping_city                  city=Sydney progress=0.0% scraper=CostOfLivingScraper
    ] studyaustralia_scrape_start    scraper=GovtScholarships
    ] Starting PhD-Seeker integration scrape scraper=PhDSeekerScraper
Error:    ] Error running PhD-Seeker: There is no current event loop in thread 'asyncio_0'. scraper=PhDSeekerScraper
Warning:  ] No data retrieved from PhD-Seeker scraper=PhDSeekerScraper
    ] phd_seeker_no_positions
    ] http_request                   response_time_ms=17.9 scraper=IDPVisaScraper status_code=403 url=https://www.idp.com/nepal/blog/latest-visa-news/
Warning:  ] http_forbidden                 scraper=IDPVisaScraper url=https://www.idp.com/nepal/blog/latest-visa-news/
    ] country_complete               country=australia nationalities=10 scraper=IDPVisaScraper
    ] scraping_visa_page             country=usa scraper=IDPVisaScraper url=https://www.idp.com/nepal/blog/usa-student-visa-requirements/
    ] http_request                   response_time_ms=8.3 scraper=IDPVisaScraper status_code=403 url=https://www.idp.com/nepal/blog/usa-student-visa-requirements/
Warning:  ] http_forbidden                 scraper=IDPVisaScraper url=https://www.idp.com/nepal/blog/usa-student-visa-requirements/
    ] country_complete               country=usa nationalities=10 scraper=IDPVisaScraper
    ] scraping_visa_page             country=uk scraper=IDPVisaScraper url=https://www.idp.com/nepal/blog/uk-student-visa-requirements/
    ] http_request                   response_time_ms=6.7 scraper=IDPVisaScraper status_code=403 url=https://www.idp.com/nepal/blog/uk-student-visa-requirements/
Warning:  ] http_forbidden                 scraper=IDPVisaScraper url=https://www.idp.com/nepal/blog/uk-student-visa-requirements/
    ] country_complete               country=uk nationalities=10 scraper=IDPVisaScraper
    ] http_request                   response_time_ms=5249.1 scraper=StudyAustraliaScholarshipScraper status_code=200 url=https://www.studyaustralia.gov.au/en/plan-your-studies/scholarships
    ] scraping_visa_page             country=canada scraper=IDPVisaScraper url=https://www.idp.com/nepal/blog/canadian-student-visa-requirements/
    ] studyaustralia_scrape_complete count=21 scraper=GovtScholarships
    ] scraper_complete               count=21 scraper=govt_scholarships
    ] http_request                   response_time_ms=39.7 scraper=IDPVisaScraper status_code=403 url=https://www.idp.com/nepal/blog/canadian-student-visa-requirements/
Warning:  ] http_forbidden                 scraper=IDPVisaScraper url=https://www.idp.com/nepal/blog/canadian-student-visa-requirements/
    ] country_complete               country=canada nationalities=10 scraper=IDPVisaScraper
    ] scraping_visa_page             country=new-zealand scraper=IDPVisaScraper url=https://www.idp.com/nepal/application-assistance/visa-news/
    ] http_request                   response_time_ms=7.4 scraper=IDPVisaScraper status_code=403 url=https://www.idp.com/nepal/application-assistance/visa-news/
Warning:  ] http_forbidden                 scraper=IDPVisaScraper url=https://www.idp.com/nepal/application-assistance/visa-news/
    ] country_complete               country=new-zealand nationalities=10 scraper=IDPVisaScraper
    ] scraping_visa_page             country=ireland scraper=IDPVisaScraper url=https://www.idp.com/nepal/blog/how-to-apply-for-an-irish-student-visa/
    ] http_request                   response_time_ms=7.4 scraper=IDPVisaScraper status_code=403 url=https://www.idp.com/nepal/blog/how-to-apply-for-an-irish-student-visa/
Warning:  ] http_forbidden                 scraper=IDPVisaScraper url=https://www.idp.com/nepal/blog/how-to-apply-for-an-irish-student-visa/
    ] country_complete               country=ireland nationalities=10 scraper=IDPVisaScraper
    ] http_request                   response_time_ms=7670.1 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Sydney
Error:    ] cost_upsert_failed             city=Sydney error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Sydney country=australia has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Melbourne progress=4.3% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=226.6 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Melbourne
Error:    ] cost_upsert_failed             city=Melbourne error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Melbourne country=australia has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Brisbane progress=8.7% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=1136.7 scraper=IDPVisaScraper status_code=200 url=https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/student-500
    ] home_affairs_accessible        scraper=IDPVisaScraper url=https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/student-500
    ] scrape_complete                scraper=IDPVisaScraper total=60
    ] scraper_complete               count=60 scraper=visa_requirements
    ] http_request                   response_time_ms=366.9 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Brisbane
Error:    ] cost_upsert_failed             city=Brisbane error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Brisbane country=australia has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Perth progress=13.0% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=367.1 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Perth
Error:    ] cost_upsert_failed             city=Perth error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Perth country=australia has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Adelaide progress=17.4% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=274.9 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Adelaide
Error:    ] cost_upsert_failed             city=Adelaide error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Adelaide country=australia has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city='Gold Coast' progress=21.7% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=140.4 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Gold-Coast
Error:    ] cost_upsert_failed             city='Gold Coast' error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city='Gold Coast' country=australia has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Canberra progress=26.1% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=139.9 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Canberra
Error:    ] cost_upsert_failed             city=Canberra error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Canberra country=australia has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=London progress=30.4% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=362.0 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/London
Error:    ] cost_upsert_failed             city=London error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=London country=uk has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Manchester progress=34.8% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=275.4 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Manchester
Error:    ] cost_upsert_failed             city=Manchester error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Manchester country=uk has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Edinburgh progress=39.1% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=359.3 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Edinburgh
Error:    ] cost_upsert_failed             city=Edinburgh error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Edinburgh country=uk has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Birmingham progress=43.5% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=274.8 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Birmingham
Error:    ] cost_upsert_failed             city=Birmingham error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Birmingham country=uk has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Glasgow progress=47.8% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=275.4 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Glasgow
Error:    ] cost_upsert_failed             city=Glasgow error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Glasgow country=uk has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Toronto progress=52.2% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=278.8 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Toronto
Error:    ] cost_upsert_failed             city=Toronto error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Toronto country=canada has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Vancouver progress=56.5% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=275.4 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Vancouver
Error:    ] cost_upsert_failed             city=Vancouver error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Vancouver country=canada has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Montreal progress=60.9% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=333.6 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Montreal
Error:    ] cost_upsert_failed             city=Montreal error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Montreal country=canada has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Calgary progress=65.2% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=276.0 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Calgary
Error:    ] cost_upsert_failed             city=Calgary error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Calgary country=canada has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city='New York' progress=69.6% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=276.7 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/New-York
Error:    ] cost_upsert_failed             city='New York' error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city='New York' country=usa has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city='Los Angeles' progress=73.9% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=360.7 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Los-Angeles
Error:    ] cost_upsert_failed             city='Los Angeles' error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city='Los Angeles' country=usa has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Boston progress=78.3% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=360.5 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Boston
Error:    ] cost_upsert_failed             city=Boston error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Boston country=usa has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Chicago progress=82.6% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=359.3 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Chicago
Error:    ] cost_upsert_failed             city=Chicago error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Chicago country=usa has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Dublin progress=87.0% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=278.4 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Dublin
Error:    ] cost_upsert_failed             city=Dublin error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Dublin country=ireland has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Cork progress=91.3% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=275.6 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Cork
Error:    ] cost_upsert_failed             city=Cork error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Cork country=ireland has_data=True scraper=CostOfLivingScraper
    ] scraping_city                  city=Galway progress=95.7% scraper=CostOfLivingScraper
    ] http_request                   response_time_ms=140.5 scraper=CostOfLivingScraper status_code=200 url=https://www.numbeo.com/cost-of-living/in/Galway
Error:    ] cost_upsert_failed             city=Galway error='Object of type datetime is not JSON serializable' scraper=CostOfLivingScraper
    ] city_complete                  city=Galway country=ireland has_data=True scraper=CostOfLivingScraper
    ] scrape_complete                scraper=CostOfLivingScraper total=23
    ] scraper_complete               count=23 scraper=cost_of_living
    ] job_complete                   counts={'idp_scholarships': 480, 'idp_courses': 6924, 'idp_universities': 768, 'visa_requirements': 60, 'cost_of_living': 23, 'govt_scholarships': 21, 'phd_seeker': 0} elapsed_minutes=5.5 elapsed_seconds=331.1 job=scrape_all_databases total=8276
📊 Post-scrape Health Report:
    ] job_start                      job=health_report
    ] health_report                  alerts=None avg_data_age_hours=116.3 counts={'scholarships': 6405, 'courses': 153648, 'universities': 1185, 'visa_requirements': 120, 'cost_of_living': 23}
    ] job_complete                   counts={'scholarships': 6405, 'courses': 153648, 'universities': 1185, 'visa_requirements': 120, 'cost_of_living': 23} elapsed_seconds=4.0 job=health_report
✅ Scrape workflow completed successfully.
2s
Post job cleanup.
/usr/bin/tar --posix -cf cache.tzst --exclude cache.tzst -P -C /home/runner/work/scholarradar/scholarradar --files-from manifest.txt --use-compress-program zstdmt
Sent 65550044 of 65550044 (100.0%), 62.5 MBs/sec
Cache saved with the key: setup-python-Linux-x64-24.04-Ubuntu-python-3.11.15-pip-38cdb11e3761bf8045f37dfdac3641a95a361120ede4e53428ccc4c8b663528a
0s
Post job cleanup.
/usr/bin/git version
git version 2.53.0
Temporarily overriding HOME='/home/runner/work/_temp/82b5a740-96f5-4983-a9c5-ec53afaa995e' before making global git config changes
Adding repository directory to the temporary git global config as a safe directory
/usr/bin/git config --global --add safe.directory /home/runner/work/scholarradar/scholarradar
/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
http.https://github.com/.extraheader
/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
0s
