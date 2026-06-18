# CHANGELOG



## [v1.1.0](https://github.com/dornech/utils-mystuff/releases/tag/v1.1.0)  (2026-06-18) 

### Bug fixes

- Corrections and edits related to Python version
(['11c79c7'](https://github.com/dornech/utils-mystuff/commit/11c79c79f2481defb2be040d78b2a339b8b2df70))
- Bug with weekday for localized dateutil.parserinfo
(['4f18224'](https://github.com/dornech/utils-mystuff/commit/4f18224b8b0f05dab76051fc6a934ac54068aee3))
- Update type annotations - do not use Callable, Optional and Union from typing.py any longer
(['40891ba'](https://github.com/dornech/utils-mystuff/commit/40891ba3e9c5027cb99f543b9ead5575c97a3ba6))
- Correct copydictfields / copy_dictfields
(['5eedb57'](https://github.com/dornech/utils-mystuff/commit/5eedb57bfd7d09bb93d606ddbc497cdb71917ca6))
- Clean-up __init__.py
(['016be0a'](https://github.com/dornech/utils-mystuff/commit/016be0a3d5f046244008847561cac15c66e08687))
- Move close_app_file from utils-mystuff to utils-mystuff-windows
(['9538b61'](https://github.com/dornech/utils-mystuff/commit/9538b6128289ac9d51483ca4566d8ae934794a24))

### Build system

- **deps**: Bump sigstore/gh-action-sigstore-python from 3.3.0 to 3.4.0
 (['6fa434e'](https://github.com/dornech/utils-mystuff/commit/6fa434e0a49c58438c8b7856143e0178d609d6ce))
- **deps**: Bump codecov/codecov-action from 6 to 7
 (['f910c1e'](https://github.com/dornech/utils-mystuff/commit/f910c1eb75cd7230709aecc562fa9d51dec965a1))
- **deps**: Bump actions/upload-pages-artifact from 4 to 5
 (['e064de9'](https://github.com/dornech/utils-mystuff/commit/e064de94bc189201ac3801f9fad642def3b46f8c))
- **deps**: Bump actions/deploy-pages from 4 to 5
 (['920c376'](https://github.com/dornech/utils-mystuff/commit/920c376ac4d5a11ffcefd13ac3676ef943258507))
- **deps**: Bump sigstore/gh-action-sigstore-python from 3.2.0 to 3.3.0
 (['69e3436'](https://github.com/dornech/utils-mystuff/commit/69e3436faeace6a61a76040c48fc1659afcc75f3))
- **deps**: Bump codecov/codecov-action from 5 to 6
 (['97445b4'](https://github.com/dornech/utils-mystuff/commit/97445b4d7325549e5685aae5450e5bb4a0e865a3))
- **deps**: Bump release-drafter/release-drafter from 6 to 7
 (['0316048'](https://github.com/dornech/utils-mystuff/commit/0316048295073f6a7fe7008f8b7a024dedb05a83))
- **deps**: Bump actions/download-artifact from 7 to 8
 (['f5224be'](https://github.com/dornech/utils-mystuff/commit/f5224be1b17ed6259811c3b06734abd289d0aee6))
- **deps**: Bump actions/upload-artifact from 6 to 7
 (['d7769f2'](https://github.com/dornech/utils-mystuff/commit/d7769f2b9be6a099b16c0e61ab27de8a0edd82cd))
- **deps**: Bump crazy-max/ghaction-github-labeler from 5.3.0 to 6.0.0
 (['6838b12'](https://github.com/dornech/utils-mystuff/commit/6838b1297abcffb61d87214f6512d3599a3e4ed1))
- **deps**: Bump actions/download-artifact from 6 to 7
 (['2fc073f'](https://github.com/dornech/utils-mystuff/commit/2fc073f94b12a33ccd5883d5839a113dcc22ba90))
- **deps**: Bump actions/upload-artifact from 5 to 6
 (['48492ff'](https://github.com/dornech/utils-mystuff/commit/48492ff0cd08510a58ba4535efdafef731f7e23a))
- **deps**: Bump sigstore/gh-action-sigstore-python from 3.1.0 to 3.2.0
 (['a4207d3'](https://github.com/dornech/utils-mystuff/commit/a4207d3bd4515fee01eed614d760b0cd5919e6b0))
- **deps**: Bump actions/checkout from 5 to 6
 (['1766f55'](https://github.com/dornech/utils-mystuff/commit/1766f55bfb80b6e26e4e56b2a1b24c25568b85c4))
- Update pyproject.toml and GitHub Action for tests - minimum Python version 3.10
(['a1827f8'](https://github.com/dornech/utils-mystuff/commit/a1827f81fef59e71e5fc8512127d9f72d28097b2))
- **deps**: Bump actions/download-artifact from 5 to 6
 (['7a967ba'](https://github.com/dornech/utils-mystuff/commit/7a967baed755015832a79b394fc904efc8fedddb))
- **deps**: Bump actions/upload-artifact from 4 to 5
 (['6f966fd'](https://github.com/dornech/utils-mystuff/commit/6f966fd1e3a459fd2c37e918c2669ef27162d1e8))
- **deps**: Bump sigstore/gh-action-sigstore-python from 3.0.1 to 3.1.0
 (['3034e4c'](https://github.com/dornech/utils-mystuff/commit/3034e4ce888c607b94af80f6223ede0a2b5c8129))
- Additional GitHub action - test documentation build
(['b5add25'](https://github.com/dornech/utils-mystuff/commit/b5add251ee043ab81d0d1848a5e49c717f5eb77b))

### Features

- Switch from mkdocs and mkdocs-theme material to properdocs with theme materialx
(['30c4351'](https://github.com/dornech/utils-mystuff/commit/30c4351600179b6ca4a750801a032d9f2c44e0ba))
- New function wait_for_file
(['4b1714c'](https://github.com/dornech/utils-mystuff/commit/4b1714cdc2a846a933df8871f80d21999e100b93))

## [v1.0.1](https://github.com/dornech/utils-mystuff/releases/tag/v1.0.1)  (2025-10-17) 

### Bug fixes

- Dummy-release for testpypi / pypi, include optional dependency for backward compatibility
(['f535766'](https://github.com/dornech/utils-mystuff/commit/f5357665a4fabf45a8a7225f8388669931b1f246))


## [v1.0.0](https://github.com/dornech/utils-mystuff/releases/tag/v1.0.0)  (2025-10-17) 

### Bug fixes

- Corrections due to problem with building documentation
(['5a4b134'](https://github.com/dornech/utils-mystuff/commit/5a4b13437547dc2538abc0990ae7b1ca03ac97a6))
- Docsig corrections
(['4e2fbbd'](https://github.com/dornech/utils-mystuff/commit/4e2fbbd7027d0bde87a29d6e13155e4dc76c9e94))
- Final clean-up before publication
(['bccba2f'](https://github.com/dornech/utils-mystuff/commit/bccba2f8198894321cea8c0fc3a1df6411d2d4f5))
- Split package in platform-dependent and windows-dependent part
(['1a65792'](https://github.com/dornech/utils-mystuff/commit/1a65792a558a0d170e0852ec0b3c7c17ec38ac7f))
- Adjustments for commitizen tool-chain
(['4613b24'](https://github.com/dornech/utils-mystuff/commit/4613b24a655eaf80e277c33b58245efeed2aea80))
- Correct .pre-commit-config.yaml
(['d8ed8db'](https://github.com/dornech/utils-mystuff/commit/d8ed8db5199792f24274d5a981ca9e33175953bd))
- Re-alignment with the-hatchlor-enhanced /2.
(['0c1cd76'](https://github.com/dornech/utils-mystuff/commit/0c1cd7668182a14691fb73dabd9ab83c3c6739a1))
- Improve type annotations and docstrings
(['7bb6114'](https://github.com/dornech/utils-mystuff/commit/7bb6114b5d3c786be3039730da74a3f802c8b363))
- Add missing docstring
(['5fd2f55'](https://github.com/dornech/utils-mystuff/commit/5fd2f55044fcbc22d29b55ee2b94dd606431177e))
- Cleanup
(['4c563f2'](https://github.com/dornech/utils-mystuff/commit/4c563f2838a795c77817fb9509590cb73472f9ff))
- Cruft settings
(['c8465da'](https://github.com/dornech/utils-mystuff/commit/c8465da53209893ae7389c9f66671d57f2f5e816))
- Re-alignment with the-hatchlor-enhanced
(['9a65134'](https://github.com/dornech/utils-mystuff/commit/9a65134d29c8f3386224f7d9f861619970609166))
- Commit after clean-up
(['ba5d5cb'](https://github.com/dornech/utils-mystuff/commit/ba5d5cb2342635f05510b3cf0b55b471d05c296a))

### Build system

- **deps**: Bump codecov/codecov-action from 4 to 5
 (['4b9060a'](https://github.com/dornech/utils-mystuff/commit/4b9060adb11aeda420a291114e55a8f60ca7d322))
- Initial commit
(['8a19bdb'](https://github.com/dornech/utils-mystuff/commit/8a19bdb5880e926fc2367a7991086b5a31c20cb7))

### Documentation


### Features

- Include new version of hatch-vcs-footgun
(['6026d7d'](https://github.com/dornech/utils-mystuff/commit/6026d7dde5c252c1bf5e85cc33fa9f4feb8c75f7))

### Initial commit

