## [**v1.1.6**]&emsp;<sub><sup>2023-08-21 ([5945384...6fda67b](https://github.com/qoomon/git-conventional-commits/compare/5945384f40e360a0c010ccefa11a553cc1a292d6...6fda67b67188520f0ac4263f53d2e1839d0133af?diff=split))</sup></sub>

### Features

- added 'Current Price' to stock data ([ab209ed](https://github.com/qoomon/git-conventional-commits/commit/ab209ed760422643fb12b6b2cecd6cf01ea8da82))

### Bug Fixes

- fixed stocks being columns instead of rows ([f5708b9](https://github.com/qoomon/git-conventional-commits/commit/f5708b9ec2e7668e1cbf6669b4001cfd4d7735a5))
- removing '\.' from field names\. ([8698887](https://github.com/qoomon/git-conventional-commits/commit/86988878bb802f7efefaedb8ee2fd236a2a115bd))

### Merges

- branch 'main' of https://github\.com/Mandy\-cyber/Yahoo\-Finance ([2919019](https://github.com/qoomon/git-conventional-commits/commit/2919019ba2baafd62fe053dd0126ebd394d3fe77))

<br>

## [**v1.1.5**]&emsp;<sub><sup>2023-07-21 ([70edd04...c9cc404](https://github.com/qoomon/git-conventional-commits/compare/70edd0474bbbbefaece16e6cdc43e12930bffa3c...c9cc4044d647b53f7d12c1ccd6e8b003f51c50c4?diff=split))</sup></sub>

### Features

- added display\_data function ([c9cc404](https://github.com/qoomon/git-conventional-commits/commit/c9cc4044d647b53f7d12c1ccd6e8b003f51c50c4))

### Bug Fixes

- fix to replace NaN values in downloaded files with 'N/A' instead ([194266d](https://github.com/qoomon/git-conventional-commits/commit/194266d750ff05a4097d5d91af5c60580ceccf87))
- fix bug where user could provide an answer other than y/n to request new ticker ([2395a20](https://github.com/qoomon/git-conventional-commits/commit/2395a20e8b326533aa48369c14b51d9efe6ed205))
- updated valid\_ticker related functions to check if ticker exists ([635beb8](https://github.com/qoomon/git-conventional-commits/commit/635beb8c6c8561d7e7be1631529536250e343778))
- fix bug where stock info was not being stored ([880824b](https://github.com/qoomon/git-conventional-commits/commit/880824bfab04a18f031388ed166758f69f39bebe))

### Merges

- branch 'main' of https://github\.com/Mandy\-cyber/Yahoo\-Finance ([9e975bd](https://github.com/qoomon/git-conventional-commits/commit/9e975bd27ce8268a4d01c07781f3a19509fce987))
- branch 'main' of https://github\.com/Mandy\-cyber/Yahoo\-Finance ([6aa7fd8](https://github.com/qoomon/git-conventional-commits/commit/6aa7fd8ca06b7ca0169ce08d2d0a8aa23f9b4898))


### BREAKING CHANGES
-  removed scrape\(\) method as instance attribute stock\_info now stores the information ([9ae7bfe](https://github.com/qoomon/git-conventional-commits/commit/9ae7bfe04fc7d087c75aefeaa933845a20176d1c))

<br>

## [**v0.1.5**]&emsp;<sub><sup>2023-07-18 ([4d20a09...e90740f](https://github.com/qoomon/git-conventional-commits/compare/4d20a0961ffd02262d26688120bb47715e655805...e90740f252f9b88b7aa84dfb18e7c76dda227c3e?diff=split))</sup></sub>

### Features

- added ability to download stock data ([02a7013](https://github.com/qoomon/git-conventional-commits/commit/02a7013b9ba86e4818139295364eca44cced79dc), [#4](https://github.com/qoomon/git-conventional-commits/issues/#4))

### Bug Fixes

- fix handshake error ([069feb6](https://github.com/qoomon/git-conventional-commits/commit/069feb6296ce1440a6a4fe27d0f8d890e8d36c63))
- fix to handle the case where a stock doesn't exist ([f3a202d](https://github.com/qoomon/git-conventional-commits/commit/f3a202d70b8c56745e8b6e5d3a9558282e39fdaa))

### Performance Improvements

- more straight\-forward page navigation ([2cc1635](https://github.com/qoomon/git-conventional-commits/commit/2cc163532a2342243df94b794885e9316ec7b055))
- remove webdriver detach option and browser navigation to homepage ([82e8d62](https://github.com/qoomon/git-conventional-commits/commit/82e8d62a21e9f07c12fdd5e68c1e4b91c89df43a))

<br>
