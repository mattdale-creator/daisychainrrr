# Proof RIP — Image Metadata Evidence Log

**Folder:** `/Users/hattr/Downloads/Proof RIP`  
**Extracted (local):** 2026-08-08 01:21:21  
**Extracted (UTC):** 2026-08-07 17:21:21Z  
**File count:** 55  
**Date range (filesystem birthtime, local):** 2026-08-08 00:04:33 → 2026-08-08 01:13:19  

## How to read this evidence

This log records **machine-readable provenance** for every image in the folder:

| Layer | What it proves | Strength |
|---|---|---|
| **SHA-256** | Exact file contents at extraction time | Strong integrity seal (any edit changes hash) |
| **Filesystem birthtime / mtime** | When this Mac first created / last modified the file | Local OS clock; can be altered by copy tools |
| **Spotlight (`mdls`)** | Indexed creation, where-from, device fields if present | Depends on what iOS/macOS wrote when importing |
| **PNG chunks (`tIME`, `tEXt`, `eXIf`)** | Embedded in-file metadata | Absent if screenshots stripped EXIF (common on iOS) |
| **xattr / quarantine / where-froms** | Download source / app provenance on this Mac | Strong for *how file arrived on this Mac* |
| **Dimensions 1284×2778** | Matches common iPhone full-screen screenshot size | Circumstantial origin (device class) |

## Collection summary

- Unique acquisition make: `['(null)']`
- Unique acquisition model: `['(null)']`
- Where-froms: `['(null)']`
- All have embedded PNG EXIF: **True**
- All have PNG tIME chunk: **False**
- All 1284×2778 RGB: **True**

## Master index (time + integrity)

| # | Filename | Bytes | Birthtime (local) | Mtime (local) | SHA-256 |
|---:|---|---:|---|---|---|
| 1 | `IMG_3305.PNG` | 514,144 | 2026-08-08 00:04:33 | 2026-08-08 00:04:33 | `82bc9ed237aeeb443ca3d2eed451cb0c6fbd4b6ddb0d88952ef8008d33342221` |
| 2 | `IMG_3306.PNG` | 524,231 | 2026-08-08 00:05:34 | 2026-08-08 00:05:34 | `b31a4f8b25a9acf7fe16d2226ae43f79e551f90a96d4726f7f0fb9196d833baf` |
| 3 | `IMG_3307.PNG` | 436,691 | 2026-08-08 00:16:28 | 2026-08-08 00:16:28 | `054c634dd9b1b9146affa0cb1e31a972b9c5ce220b9c615b2f94aa97d6f94010` |
| 4 | `IMG_3308.PNG` | 489,577 | 2026-08-08 00:21:46 | 2026-08-08 00:21:46 | `3bb3b28f8fe4f405e7cd07675a3e23b77d99e8f6613523e60a180dc6494ca6cb` |
| 5 | `IMG_3309.PNG` | 735,173 | 2026-08-08 01:01:46 | 2026-08-08 01:01:46 | `e574026be41b632f05d08fbaed797fa48f51a69ac2eaf7dc0c2ffad71f367a99` |
| 6 | `IMG_3310.PNG` | 583,421 | 2026-08-08 01:02:53 | 2026-08-08 01:02:53 | `33ce1c1d49a3034a816d9f19f2cb2b1c1e1a37d068f8c1ee0375bfcbfaefa98a` |
| 7 | `IMG_3311.PNG` | 454,490 | 2026-08-08 01:03:01 | 2026-08-08 01:03:01 | `1f3b07ba0b26628936fc973c0bc4dfb0fdb4b5a03c26c36f03b520ab62d1f8b4` |
| 8 | `IMG_3312.PNG` | 414,405 | 2026-08-08 01:03:04 | 2026-08-08 01:03:04 | `0ba69ee3ecae5d97855ec3b891e57b08d5bfc6adcd2c9652495c0aa8e865a704` |
| 9 | `IMG_3313.PNG` | 518,100 | 2026-08-08 01:04:08 | 2026-08-08 01:04:08 | `0cb5d8b359c40d78a773e7bd93aaa890f091406ab2ce6dd98c772c6bfbbc16d6` |
| 10 | `IMG_3314.PNG` | 496,485 | 2026-08-08 01:04:14 | 2026-08-08 01:04:14 | `75dba17f6856cccb46bfbb157e6cc3bb473dd0f12b18e399bf6af1aeaa5b675e` |
| 11 | `IMG_3315.PNG` | 538,996 | 2026-08-08 01:04:17 | 2026-08-08 01:04:17 | `84c456e0c318fd92d777a91cf1efb9a3a7aedb33ee58456b2c77e9ba7b23eeef` |
| 12 | `IMG_3316.PNG` | 488,567 | 2026-08-08 01:04:20 | 2026-08-08 01:04:20 | `ae92643d459d6b2c3740fa99c0a7555ab154172dd8a1a742f42a74fdd9d9edb5` |
| 13 | `IMG_3317.PNG` | 431,152 | 2026-08-08 01:04:21 | 2026-08-08 01:04:21 | `c364c27a66992e3e012eb98fd5a4d04533bb1db746dd7b133c155e2deed8be50` |
| 14 | `IMG_3318.PNG` | 435,336 | 2026-08-08 01:05:05 | 2026-08-08 01:05:05 | `e80fb769c4d50758bd40fe4b58a1efb18b16aa2a022ee2d198f9d91a0bd51cd4` |
| 15 | `IMG_3319.PNG` | 414,512 | 2026-08-08 01:05:22 | 2026-08-08 01:05:22 | `2cd730da1cdc3723bb23f6ab9c293c728d2d5e94f40ff3b5860a3b2c19d42dc8` |
| 16 | `IMG_3320.PNG` | 528,158 | 2026-08-08 01:05:52 | 2026-08-08 01:05:52 | `ee27692c450252169875b5f32e285439bd425afe3c6378f872a2c65186d963ef` |
| 17 | `IMG_3321.PNG` | 401,679 | 2026-08-08 01:05:56 | 2026-08-08 01:05:56 | `86211ea3202f2b28db7d796537e0a9e1b28e2e8f2d2245400ff9f92a7229e534` |
| 18 | `IMG_3322.PNG` | 371,890 | 2026-08-08 01:05:58 | 2026-08-08 01:05:58 | `dbcda0432826189b083c53ae69eaf269f97e9f873e1dc0ce545b09dfbb785b97` |
| 19 | `IMG_3323.PNG` | 386,185 | 2026-08-08 01:06:13 | 2026-08-08 01:06:13 | `84f02f25ab82f814f544093ada97a4bdaaecc82a2c7844425d34af0d20d38f58` |
| 20 | `IMG_3324.PNG` | 533,336 | 2026-08-08 01:06:15 | 2026-08-08 01:06:15 | `5e4e7ad9d5ef5d23cc0bd14704c0c38197e0e448f07bc0833bf0e0dc682d39cb` |
| 21 | `IMG_3325.PNG` | 370,717 | 2026-08-08 01:06:20 | 2026-08-08 01:06:20 | `83b8b9257e3bba655e06f79c40fd096ab8d5f675766316321712dd52425f35f6` |
| 22 | `IMG_3326.PNG` | 471,853 | 2026-08-08 01:06:29 | 2026-08-08 01:06:29 | `2efb83c102fa9e0ed2cdebf887014e3d771f9070de23728e7ab79cf8159ee9a3` |
| 23 | `IMG_3327.PNG` | 497,445 | 2026-08-08 01:06:34 | 2026-08-08 01:06:34 | `7546bdbf738ece9d5d8eadafba50909ac6193455c1390d3894b00e64b4b327d3` |
| 24 | `IMG_3328.PNG` | 471,802 | 2026-08-08 01:06:37 | 2026-08-08 01:06:37 | `4f104cddf40a3a13cd4ade39c37cec0d2c8842860fb47c275a6d8afb0c09720d` |
| 25 | `IMG_3329.PNG` | 509,774 | 2026-08-08 01:06:39 | 2026-08-08 01:06:39 | `299246ca29b62696a07fe8a3dc44842f541c886c8138140c81b998c176dcd1b8` |
| 26 | `IMG_3330.PNG` | 499,427 | 2026-08-08 01:06:41 | 2026-08-08 01:06:41 | `0028060f0caee1d0d88f7fcecc03105157b6f65477bf38cb1100845a2c7c7c62` |
| 27 | `IMG_3331.PNG` | 449,607 | 2026-08-08 01:06:43 | 2026-08-08 01:06:43 | `1934e006391d0a4f4dad006206e81cccbe5e38b1778b85f363f5e490b5663ca0` |
| 28 | `IMG_3332.PNG` | 465,238 | 2026-08-08 01:06:44 | 2026-08-08 01:06:44 | `d51cb0ff2a88566b6bd02177f67ab63333b5c58f633ebdc5261b3de775d9512b` |
| 29 | `IMG_3333.PNG` | 457,986 | 2026-08-08 01:06:46 | 2026-08-08 01:06:46 | `4e994977cc161a4bb9d0be618e950c8b865d0495ee4741831fabb3a41c6e43b0` |
| 30 | `IMG_3334.PNG` | 523,015 | 2026-08-08 01:06:48 | 2026-08-08 01:06:48 | `a66ab1342d0a9654be86c18e78cb35edee056c899597d1da3d4e9e6419142aeb` |
| 31 | `IMG_3335.PNG` | 517,206 | 2026-08-08 01:06:50 | 2026-08-08 01:06:50 | `b4f1b5d8d4c50c6ae7b272f73d1072bf14e8d0eee4b146eadee1419abe643417` |
| 32 | `IMG_3336.PNG` | 456,904 | 2026-08-08 01:06:52 | 2026-08-08 01:06:52 | `fb098e752fe5a727a1b82bc3b14a48f893ecd914d5054fd77ed389a4828222a5` |
| 33 | `IMG_3337.PNG` | 511,895 | 2026-08-08 01:06:54 | 2026-08-08 01:06:54 | `90d2cc09f85ede4d0d9d606cab685dbc50c853ef9614fe3cf4b84a9373daab62` |
| 34 | `IMG_3338.PNG` | 521,289 | 2026-08-08 01:06:56 | 2026-08-08 01:06:56 | `d001c7de3c4855133ac8722f11a6842989c35833e89c31d752a4a0feb7f03638` |
| 35 | `IMG_3339.PNG` | 487,305 | 2026-08-08 01:06:59 | 2026-08-08 01:06:59 | `fb3de90c23e180e4f2f9efbd44fb294cda2ddede9a7283586e11165e060550e5` |
| 36 | `IMG_3340.PNG` | 441,869 | 2026-08-08 01:07:02 | 2026-08-08 01:07:02 | `55ee702047cefd318b8e51d65f0f1901715b014349bc7a666abcd3e63540dfb6` |
| 37 | `IMG_3341.PNG` | 436,920 | 2026-08-08 01:07:04 | 2026-08-08 01:07:04 | `256ef7154c6c1947b0799b52993d070e75388dcb33f1e7992a2bd7764f39fd5a` |
| 38 | `IMG_3342.PNG` | 455,439 | 2026-08-08 01:07:06 | 2026-08-08 01:07:06 | `47f5b2beed02ee0f2cf45fb810016803331fe9386a8636347968918a534ba521` |
| 39 | `IMG_3343.PNG` | 457,682 | 2026-08-08 01:07:08 | 2026-08-08 01:07:08 | `871bfb81ec9de2427854e60d660c8091362d4d6bb87b4bfd3762799ff42ece4d` |
| 40 | `IMG_3344.PNG` | 471,544 | 2026-08-08 01:07:10 | 2026-08-08 01:07:10 | `f10046f921f4dd1b6c8c71f326373434956d9b0d830b7239f9ffed7959b5fa7b` |
| 41 | `IMG_3345.PNG` | 469,773 | 2026-08-08 01:07:11 | 2026-08-08 01:07:11 | `e5bea6a3005208c3c4cfe3506a733646a5607f9083ccf19695eac0d9ff19cc96` |
| 42 | `IMG_3346.PNG` | 455,903 | 2026-08-08 01:07:16 | 2026-08-08 01:07:16 | `26caf788c9ae3a07030e46e905a88e8eccfb677aba036064c0c408430b70d1ea` |
| 43 | `IMG_3347.PNG` | 473,357 | 2026-08-08 01:07:18 | 2026-08-08 01:07:18 | `9ed00b4898ae60ce5eb2be55c7ac9753c56f79ab74ea69c9a8e77324ebff0715` |
| 44 | `IMG_3348.PNG` | 467,646 | 2026-08-08 01:07:21 | 2026-08-08 01:07:21 | `ed2b6b4e1fb1d2e1ddb6049d4b4254cebec9674d7ce319308f1fb6547d9c476c` |
| 45 | `IMG_3349.PNG` | 497,240 | 2026-08-08 01:07:23 | 2026-08-08 01:07:23 | `58811eff200e26d779c4230e53bd06525d5e4cce5d24be3ec4923469c005c2cd` |
| 46 | `IMG_3350.PNG` | 514,994 | 2026-08-08 01:07:26 | 2026-08-08 01:07:26 | `74d196529d41f9ea2b92de3f0e67a063deee4a6df8c438a0ecab6af8cb0516c0` |
| 47 | `IMG_3351.PNG` | 455,690 | 2026-08-08 01:07:28 | 2026-08-08 01:07:28 | `3c926dd23da799c6cff6906e8a6e724f6865af248496e0791d4a0832617c0211` |
| 48 | `IMG_3352.PNG` | 507,399 | 2026-08-08 01:07:31 | 2026-08-08 01:07:31 | `bd715d65667db81531814a179d72bd12b7f7bd5df51c3edabcb6e67a6f1c1594` |
| 49 | `IMG_3353.PNG` | 484,538 | 2026-08-08 01:07:33 | 2026-08-08 01:07:33 | `7ad94a4d10b415df2b9228fa21f21f962e4b7b56fb7c2843372253502480590d` |
| 50 | `IMG_3354.PNG` | 400,140 | 2026-08-08 01:07:35 | 2026-08-08 01:07:35 | `b5388773afb85df91f15d7b276db011e48f4a3d4de5947c25fb06b50571c62bc` |
| 51 | `IMG_3355.PNG` | 420,553 | 2026-08-08 01:07:38 | 2026-08-08 01:07:38 | `d75b5ac82795db95d8993604e1fb9c4af4b01463d641a32d6d5c65d889a9585a` |
| 52 | `IMG_3356.PNG` | 484,856 | 2026-08-08 01:07:40 | 2026-08-08 01:07:40 | `7a5535efc9d736a047a2e53783aa6441f7f5255ade770f2bcf2c41c0e7d29f88` |
| 53 | `IMG_3357.PNG` | 522,303 | 2026-08-08 01:07:42 | 2026-08-08 01:07:42 | `12032fd3eccca4cf5a9a6e96154ef4dda19bc6b69f73dde5150a27d9ae102ce9` |
| 54 | `IMG_3358.PNG` | 532,686 | 2026-08-08 01:07:45 | 2026-08-08 01:07:45 | `f4159cfe4f295825b3b9baae331d8ae9a32099403182bc94de903428cccf2c91` |
| 55 | `IMG_3359.PNG` | 2,569,646 | 2026-08-08 01:13:19 | 2026-08-08 01:13:19 | `93dbc26c54828d1cfef0ac615a2ff755da7a5a4d8ef6638735b75adc6e05eba3` |

## Per-file full metadata

### 1. `IMG_3305.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3305.PNG`
- **SHA-256:** `82bc9ed237aeeb443ca3d2eed451cb0c6fbd4b6ddb0d88952ef8008d33342221`
- **Size:** 514,144 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 00:04:33 / 2026-08-07 16:04:33Z
- **Filesystem mtime (local / UTC):** 2026-08-08 00:04:33 / 2026-08-07 16:04:33Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T00:04:33</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 16:04:33 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 16:04:33 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 16:04:33 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 16:04:33 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 514144
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '69 65 B7 CE 75 1C 49 19 A7 B1 97 B1 D7 6A 65 33'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 1C C8 DF EE 78 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `6965B7CE-751C-4919-A7B1-97B1D76A6533
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 1C C8 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3305.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;9A966D24-2449-4EE0-9631-A5BDB80C7862\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 39 41 39 36 36 44 32 34 2D 32 34 34 39 2D 34 45 45 '}`

### 2. `IMG_3306.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3306.PNG`
- **SHA-256:** `b31a4f8b25a9acf7fe16d2226ae43f79e551f90a96d4726f7f0fb9196d833baf`
- **Size:** 524,231 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 00:05:34 / 2026-08-07 16:05:34Z
- **Filesystem mtime (local / UTC):** 2026-08-08 00:05:34 / 2026-08-07 16:05:34Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T00:05:34</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 16:05:34 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 16:05:34 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 16:05:34 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 16:05:34 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 524231
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'BB D7 A7 A9 CE CF 4E FF 9D EA 46 66 45 1B 30 34'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 1C E7 10 88 37 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `BBD7A7A9-CECF-4EFF-9DEA-4666451B3034
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 1C E7 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3306.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;B436BF3A-CACE-4530-AFED-E78B494DD173\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 42 34 33 36 42 46 33 41 2D 43 41 43 45 2D 34 35 33 '}`

### 3. `IMG_3307.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3307.PNG`
- **SHA-256:** `054c634dd9b1b9146affa0cb1e31a972b9c5ce220b9c615b2f94aa97d6f94010`
- **Size:** 436,691 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 00:16:28 / 2026-08-07 16:16:28Z
- **Filesystem mtime (local / UTC):** 2026-08-08 00:16:28 / 2026-08-07 16:16:28Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T00:16:28</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 16:16:28 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 16:16:28 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 16:16:28 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 16:16:28 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 436691
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'A9 83 CF B1 FF 13 48 9C A6 C7 A9 8D 63 1E 1D D9'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 1E 2E 28 8B FC 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `A983CFB1-FF13-489C-A6C7-A98D631E1DD9
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 1E 2E 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3307.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;0B59F7AA-104A-46AF-96BC-17B6C14462C3\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 30 42 35 39 46 37 41 41 2D 31 30 34 41 2D 34 36 41 '}`

### 4. `IMG_3308.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3308.PNG`
- **SHA-256:** `3bb3b28f8fe4f405e7cd07675a3e23b77d99e8f6613523e60a180dc6494ca6cb`
- **Size:** 489,577 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 00:21:46 / 2026-08-07 16:21:46Z
- **Filesystem mtime (local / UTC):** 2026-08-08 00:21:46 / 2026-08-07 16:21:46Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T00:21:46</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 16:21:46 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 16:21:46 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 16:21:46 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 16:21:46 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 489577
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'CD 5F E3 65 97 67 4B 54 81 AF 9B 57 B1 90 01 9D'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 1E CD 22 E5 82 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `CD5FE365-9767-4B54-81AF-9B57B190019D
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 1E CD 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3308.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;9F58E277-DE12-4A21-B1EA-4B6FDC6D05A1\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 39 46 35 38 45 32 37 37 2D 44 45 31 32 2D 34 41 32 '}`

### 5. `IMG_3309.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3309.PNG`
- **SHA-256:** `e574026be41b632f05d08fbaed797fa48f51a69ac2eaf7dc0c2ffad71f367a99`
- **Size:** 735,173 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:01:46 / 2026-08-07 17:01:46Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:01:46 / 2026-08-07 17:01:46Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:01:46</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:01:46 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:01:46 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:01:46 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:01:46 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 735173
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '4C 34 08 0A 16 D6 4D C2 B0 0F C7 9B 58 22 3A 5E'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 7D 7E 3C B0 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `4C34080A-16D6-4DC2-B00F-C79B58223A5E
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 7D 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3309.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;9C512A52-7DD1-4DA6-BF06-5D122BA77F9D\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 39 43 35 31 32 41 35 32 2D 37 44 44 31 2D 34 44 41 '}`

### 6. `IMG_3310.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3310.PNG`
- **SHA-256:** `33ce1c1d49a3034a816d9f19f2cb2b1c1e1a37d068f8c1ee0375bfcbfaefa98a`
- **Size:** 583,421 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:02:53 / 2026-08-07 17:02:53Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:02:53 / 2026-08-07 17:02:53Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:02:53</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:02:53 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:02:53 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:02:53 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:02:53 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 583421
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'EC 90 DE 5A 4A C0 4C E5 B5 77 73 C1 EB F9 41 73'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 9E EF 37 65 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `EC90DE5A-4AC0-4CE5-B577-73C1EBF94173
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 9E 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3310.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;96F3DE85-ECA9-4BE2-84EF-B0F50BE6D219\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 39 36 46 33 44 45 38 35 2D 45 43 41 39 2D 34 42 45 '}`

### 7. `IMG_3311.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3311.PNG`
- **SHA-256:** `1f3b07ba0b26628936fc973c0bc4dfb0fdb4b5a03c26c36f03b520ab62d1f8b4`
- **Size:** 454,490 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:03:01 / 2026-08-07 17:03:01Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:03:01 / 2026-08-07 17:03:01Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:03:01</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:03:01 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:03:01 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:03:01 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:03:01 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 454490
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'D3 77 98 05 A7 25 4B 73 8E DC C0 CD AF CF 7F 8B'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 A2 96 F6 83 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `D3779805-A725-4B73-8EDC-C0CDAFCF7F8B
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 A2 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3311.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;9F2BDF52-BD22-48C7-9253-D73F41056A79\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 39 46 32 42 44 46 35 32 2D 42 44 32 32 2D 34 38 43 '}`

### 8. `IMG_3312.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3312.PNG`
- **SHA-256:** `0ba69ee3ecae5d97855ec3b891e57b08d5bfc6adcd2c9652495c0aa8e865a704`
- **Size:** 414,405 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:03:04 / 2026-08-07 17:03:04Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:03:04 / 2026-08-07 17:03:04Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:03:04</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:03:04 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:03:04 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:03:04 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:03:04 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 414405
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'EF F9 AC FE E5 61 49 69 9F 32 D5 CE C5 EF B1 DE'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 A4 69 B0 0C 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `EFF9ACFE-E561-4969-9F32-D5CEC5EFB1DE
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 A4 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3312.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;97951AD3-6850-4395-8E23-EB981E29528C\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 39 37 39 35 31 41 44 33 2D 36 38 35 30 2D 34 33 39 '}`

### 9. `IMG_3313.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3313.PNG`
- **SHA-256:** `0cb5d8b359c40d78a773e7bd93aaa890f091406ab2ce6dd98c772c6bfbbc16d6`
- **Size:** 518,100 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:04:08 / 2026-08-07 17:04:08Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:04:08 / 2026-08-07 17:04:08Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:04:08</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:04:08 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:04:08 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:04:08 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:04:08 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 518100
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '73 52 78 AD EB 5B 4D 6C B1 D2 53 AA B9 AF F7 92'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 C4 69 EC 89 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `735278AD-EB5B-4D6C-B1D2-53AAB9AFF792
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 C4 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3313.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;89265280-A418-41A6-977E-4233F54291DA\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 38 39 32 36 35 32 38 30 2D 41 34 31 38 2D 34 31 41 '}`

### 10. `IMG_3314.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3314.PNG`
- **SHA-256:** `75dba17f6856cccb46bfbb157e6cc3bb473dd0f12b18e399bf6af1aeaa5b675e`
- **Size:** 496,485 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:04:14 / 2026-08-07 17:04:14Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:04:14 / 2026-08-07 17:04:14Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:04:14</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:04:14 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:04:14 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:04:14 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:04:14 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 496485
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '07 3C B3 9B F2 A8 43 A1 B8 A6 C8 CE 2B 9F E0 28'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 C7 38 CA CD 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `073CB39B-F2A8-43A1-B8A6-C8CE2B9FE028
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 C7 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3314.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;72CF01FB-AE04-4831-B6F9-B60413EB4AE3\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 37 32 43 46 30 31 46 42 2D 41 45 30 34 2D 34 38 33 '}`

### 11. `IMG_3315.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3315.PNG`
- **SHA-256:** `84c456e0c318fd92d777a91cf1efb9a3a7aedb33ee58456b2c77e9ba7b23eeef`
- **Size:** 538,996 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:04:17 / 2026-08-07 17:04:17Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:04:17 / 2026-08-07 17:04:17Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:04:17</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:04:17 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:04:17 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:04:17 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:04:17 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 538996
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '97 84 58 ED 04 57 44 65 B9 90 AD 37 C2 AB FC 6A'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 C8 AE DF 40 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `978458ED-0457-4465-B990-AD37C2ABFC6A
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 C8 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3315.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;473B2A02-8D48-4ABF-9969-02CDCED3FEFE\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 34 37 33 42 32 41 30 32 2D 38 44 34 38 2D 34 41 42 '}`

### 12. `IMG_3316.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3316.PNG`
- **SHA-256:** `ae92643d459d6b2c3740fa99c0a7555ab154172dd8a1a742f42a74fdd9d9edb5`
- **Size:** 488,567 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:04:20 / 2026-08-07 17:04:20Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:04:20 / 2026-08-07 17:04:20Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:04:20</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:04:20 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:04:20 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:04:20 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:04:20 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 488567
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '3B 04 B8 4D DC BD 48 A6 A7 FB F4 52 A9 9D 4C D2'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 CA 38 44 E9 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `3B04B84D-DCBD-48A6-A7FB-F452A99D4CD2
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 CA 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3316.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;E54DFE9B-74AA-4E73-B056-68412BFBBA77\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 45 35 34 44 46 45 39 42 2D 37 34 41 41 2D 34 45 37 '}`

### 13. `IMG_3317.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3317.PNG`
- **SHA-256:** `c364c27a66992e3e012eb98fd5a4d04533bb1db746dd7b133c155e2deed8be50`
- **Size:** 431,152 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:04:21 / 2026-08-07 17:04:21Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:04:21 / 2026-08-07 17:04:21Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:04:21</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:04:21 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:04:21 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:04:21 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:04:21 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 431152
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '6F 2A 0B 51 92 34 46 AA BE 7C C5 85 6E CD 40 A2'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 CB 05 9B CC 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `6F2A0B51-9234-46AA-BE7C-C5856ECD40A2
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 CA 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3317.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;ED11414C-83A6-4DD2-ABA6-D0FA682B8966\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 45 44 31 31 34 31 34 43 2D 38 33 41 36 2D 34 44 44 '}`

### 14. `IMG_3318.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3318.PNG`
- **SHA-256:** `e80fb769c4d50758bd40fe4b58a1efb18b16aa2a022ee2d198f9d91a0bd51cd4`
- **Size:** 435,336 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:05:05 / 2026-08-07 17:05:05Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:05:05 / 2026-08-07 17:05:05Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:05:05</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:05:05 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:05:05 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:05:05 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:05:05 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 435336
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '72 FA 3C 3C DD 7A 40 EC B9 CB 18 0E 8D 5D 34 98'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 E0 FA 1A 26 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `72FA3C3C-DD7A-40EC-B9CB-180E8D5D3498
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 E0 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3318.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;3ED8BC45-13C3-47D9-BEE9-2A02C30A85AC\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 33 45 44 38 42 43 34 35 2D 31 33 43 33 2D 34 37 44 '}`

### 15. `IMG_3319.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3319.PNG`
- **SHA-256:** `2cd730da1cdc3723bb23f6ab9c293c728d2d5e94f40ff3b5860a3b2c19d42dc8`
- **Size:** 414,512 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:05:22 / 2026-08-07 17:05:22Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:05:22 / 2026-08-07 17:05:22Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:05:22</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:05:22 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:05:22 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:05:22 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:05:22 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 414512
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'E0 01 A8 3B 0D E7 45 D9 A0 87 AC F7 B8 C4 14 F0'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 E9 40 CE D5 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `E001A83B-0DE7-45D9-A087-ACF7B8C414F0
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 E9 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3319.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;CBD44F11-396B-49B5-A7BB-5222257F164C\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 43 42 44 34 34 46 31 31 2D 33 39 36 42 2D 34 39 42 '}`

### 16. `IMG_3320.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3320.PNG`
- **SHA-256:** `ee27692c450252169875b5f32e285439bd425afe3c6378f872a2c65186d963ef`
- **Size:** 528,158 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:05:52 / 2026-08-07 17:05:52Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:05:52 / 2026-08-07 17:05:52Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:05:52</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:05:52 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:05:52 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:05:52 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:05:52 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 528158
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '9C 22 E0 0A 74 CF 49 0E AB E3 BA 37 A0 A5 2A 53'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 F8 1D 39 8F 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `9C22E00A-74CF-490E-ABE3-BA37A0A52A53
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 F8 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3320.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;E24C3CC6-DEF6-454A-B6D0-94707B044ED2\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 45 32 34 43 33 43 43 36 2D 44 45 46 36 2D 34 35 34 '}`

### 17. `IMG_3321.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3321.PNG`
- **SHA-256:** `86211ea3202f2b28db7d796537e0a9e1b28e2e8f2d2245400ff9f92a7229e534`
- **Size:** 401,679 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:05:56 / 2026-08-07 17:05:56Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:05:56 / 2026-08-07 17:05:56Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:05:56</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:05:56 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:05:56 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:05:56 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:05:56 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 401679
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'A8 07 A4 2F CB 7E 48 E3 89 81 56 83 6C CC C4 90'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 FA 0F 06 D5 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `A807A42F-CB7E-48E3-8981-56836CCCC490
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 FA 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3321.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;B5BBEC2F-A59D-47DF-874E-A9711501E1F3\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 42 35 42 42 45 43 32 46 2D 41 35 39 44 2D 34 37 44 '}`

### 18. `IMG_3322.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3322.PNG`
- **SHA-256:** `dbcda0432826189b083c53ae69eaf269f97e9f873e1dc0ce545b09dfbb785b97`
- **Size:** 371,890 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:05:58 / 2026-08-07 17:05:58Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:05:58 / 2026-08-07 17:05:58Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:05:58</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:05:58 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:05:58 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:05:58 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:05:58 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 371890
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '18 80 38 0C E7 7A 45 DC 9D AD 3D 64 75 3E 23 25'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 FB 14 DB BE 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `1880380C-E77A-45DC-9DAD-3D64753E2325
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 23 FB 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3322.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;61FFD8C1-D07B-4821-86DC-C29928B35B7A\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 36 31 46 46 44 38 43 31 2D 44 30 37 42 2D 34 38 32 '}`

### 19. `IMG_3323.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3323.PNG`
- **SHA-256:** `84f02f25ab82f814f544093ada97a4bdaaecc82a2c7844425d34af0d20d38f58`
- **Size:** 386,185 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:13 / 2026-08-07 17:06:13Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:13 / 2026-08-07 17:06:13Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:13</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:13 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:13 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:13 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:13 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 386185
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '83 E6 26 CD 9F E5 47 D4 9C BD CD 0A 42 89 81 A3'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 02 AA 80 84 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `83E626CD-9FE5-47D4-9CBD-CD0A428981A3
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 02 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3323.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;9E98B331-0B7D-42AD-BC53-1A22CCE958C9\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 39 45 39 38 42 33 33 31 2D 30 42 37 44 2D 34 32 41 '}`

### 20. `IMG_3324.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3324.PNG`
- **SHA-256:** `5e4e7ad9d5ef5d23cc0bd14704c0c38197e0e448f07bc0833bf0e0dc682d39cb`
- **Size:** 533,336 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:15 / 2026-08-07 17:06:15Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:15 / 2026-08-07 17:06:15Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:15</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:15 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:15 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:15 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:15 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 533336
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '28 09 37 48 84 14 4F 52 90 A7 0D 74 92 60 00 40'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 03 DA 19 5D 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `28093748-8414-4F52-90A7-0D7492600040
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 03 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3324.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;4F4CDC45-E888-4CFA-8B2A-0D2E51FDB9BA\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 34 46 34 43 44 43 34 35 2D 45 38 38 38 2D 34 43 46 '}`

### 21. `IMG_3325.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3325.PNG`
- **SHA-256:** `83b8b9257e3bba655e06f79c40fd096ab8d5f675766316321712dd52425f35f6`
- **Size:** 370,717 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:20 / 2026-08-07 17:06:20Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:20 / 2026-08-07 17:06:20Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:20</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:20 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:20 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:20 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:20 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 370717
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'B7 25 19 2C A4 05 4A 3E 85 8E 22 29 D9 76 1D 17'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 06 55 1D 36 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `B725192C-A405-4A3E-858E-2229D9761D17
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 06 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3325.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;8EE9A93C-B3D1-4F12-89FF-AE095F7560CC\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 38 45 45 39 41 39 33 43 2D 42 33 44 31 2D 34 46 31 '}`

### 22. `IMG_3326.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3326.PNG`
- **SHA-256:** `2efb83c102fa9e0ed2cdebf887014e3d771f9070de23728e7ab79cf8159ee9a3`
- **Size:** 471,853 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:29 / 2026-08-07 17:06:29Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:29 / 2026-08-07 17:06:29Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:29</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:29 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:29 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:29 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:29 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 471853
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '45 80 6C 23 41 37 41 27 B6 27 AB 72 FA E2 54 C6'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 0A B6 16 94 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `45806C23-4137-4127-B627-AB72FAE254C6
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 0A 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3326.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;1C1C1113-37AD-4C23-B8C4-BFBC633B14F2\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 31 43 31 43 31 31 31 33 2D 33 37 41 44 2D 34 43 32 '}`

### 23. `IMG_3327.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3327.PNG`
- **SHA-256:** `7546bdbf738ece9d5d8eadafba50909ac6193455c1390d3894b00e64b4b327d3`
- **Size:** 497,445 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:34 / 2026-08-07 17:06:34Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:34 / 2026-08-07 17:06:34Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:34</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:34 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:34 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:34 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:34 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 497445
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'AC E5 49 E1 EB 61 44 5D 97 AF D0 4E ED 15 D6 B5'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 0D 6F DE F0 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `ACE549E1-EB61-445D-97AF-D04EED15D6B5
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 0D 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3327.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;C011BB63-D79A-436D-A51A-32E18DE85005\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 43 30 31 31 42 42 36 33 2D 44 37 39 41 2D 34 33 36 '}`

### 24. `IMG_3328.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3328.PNG`
- **SHA-256:** `4f104cddf40a3a13cd4ade39c37cec0d2c8842860fb47c275a6d8afb0c09720d`
- **Size:** 471,802 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:37 / 2026-08-07 17:06:37Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:37 / 2026-08-07 17:06:37Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:37</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:37 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:37 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:37 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:37 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 471802
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'DB 89 34 FB 68 E3 49 FA B7 9F DF C5 E5 8D 23 D3'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 0E 99 1A 5D 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `DB8934FB-68E3-49FA-B79F-DFC5E58D23D3
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 0E 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3328.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;E46D3131-35EB-41AC-9140-3D325665CDAD\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 45 34 36 44 33 31 33 31 2D 33 35 45 42 2D 34 31 41 '}`

### 25. `IMG_3329.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3329.PNG`
- **SHA-256:** `299246ca29b62696a07fe8a3dc44842f541c886c8138140c81b998c176dcd1b8`
- **Size:** 509,774 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:39 / 2026-08-07 17:06:39Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:39 / 2026-08-07 17:06:39Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:39</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:39 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:39 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:39 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:39 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 509774
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '3C AB A3 EE CC F5 4E 24 9A 24 5A E5 FD 31 34 B1'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 0F BC 50 0D 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `3CABA3EE-CCF5-4E24-9A24-5AE5FD3134B1
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 0F 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3329.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;E01C926C-5BB3-4F3C-9036-69045752CEB6\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 45 30 31 43 39 32 36 43 2D 35 42 42 33 2D 34 46 33 '}`

### 26. `IMG_3330.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3330.PNG`
- **SHA-256:** `0028060f0caee1d0d88f7fcecc03105157b6f65477bf38cb1100845a2c7c7c62`
- **Size:** 499,427 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:41 / 2026-08-07 17:06:41Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:41 / 2026-08-07 17:06:41Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:41</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:41 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:41 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:41 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:41 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 499427
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'BB 45 28 BD 07 CE 4F DC A8 4C 42 57 52 10 EC 2F'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 10 CC 9B 74 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `BB4528BD-07CE-4FDC-A84C-42575210EC2F
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 10 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3330.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;5556D466-015D-4DFC-8E29-999B644C83BB\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 35 35 35 36 44 34 36 36 2D 30 31 35 44 2D 34 44 46 '}`

### 27. `IMG_3331.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3331.PNG`
- **SHA-256:** `1934e006391d0a4f4dad006206e81cccbe5e38b1778b85f363f5e490b5663ca0`
- **Size:** 449,607 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:43 / 2026-08-07 17:06:43Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:43 / 2026-08-07 17:06:43Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:43</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:43 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:43 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:43 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:43 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 449607
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'A6 9E 87 81 C5 78 4F F5 9F 76 C3 4F 58 4C E1 1E'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 11 AA F1 CC 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `A69E8781-C578-4FF5-9F76-C34F584CE11E
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 11 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3331.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;B6900E5E-B123-4AAF-9EAA-EB8B8C98397C\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 42 36 39 30 30 45 35 45 2D 42 31 32 33 2D 34 41 41 '}`

### 28. `IMG_3332.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3332.PNG`
- **SHA-256:** `d51cb0ff2a88566b6bd02177f67ab63333b5c58f633ebdc5261b3de775d9512b`
- **Size:** 465,238 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:44 / 2026-08-07 17:06:44Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:44 / 2026-08-07 17:06:44Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:44</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:44 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:44 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:44 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:44 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 465238
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '0F E5 BE 79 34 76 45 C5 85 2E 68 34 6C B2 3B CC'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 12 80 93 53 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `0FE5BE79-3476-45C5-852E-68346CB23BCC
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 12 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3332.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;67603C8D-E1A7-42BD-AA02-856298130E31\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 36 37 36 30 33 43 38 44 2D 45 31 41 37 2D 34 32 42 '}`

### 29. `IMG_3333.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3333.PNG`
- **SHA-256:** `4e994977cc161a4bb9d0be618e950c8b865d0495ee4741831fabb3a41c6e43b0`
- **Size:** 457,986 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:46 / 2026-08-07 17:06:46Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:46 / 2026-08-07 17:06:46Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:46</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:46 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:46 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:46 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:46 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 457986
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'F2 4F B9 F0 04 09 42 0C 95 88 8F 9B 1B 5D 05 DE'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 13 49 12 A1 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `F24FB9F0-0409-420C-9588-8F9B1B5D05DE
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 13 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3333.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;965BB5E8-360D-48DA-908E-7A45C8BF3480\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 39 36 35 42 42 35 45 38 2D 33 36 30 44 2D 34 38 44 '}`

### 30. `IMG_3334.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3334.PNG`
- **SHA-256:** `a66ab1342d0a9654be86c18e78cb35edee056c899597d1da3d4e9e6419142aeb`
- **Size:** 523,015 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:48 / 2026-08-07 17:06:48Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:48 / 2026-08-07 17:06:48Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:48</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:48 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:48 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:48 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:48 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 523015
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '39 20 C9 85 F4 04 43 92 A6 42 11 EC 49 EA 06 66'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 14 35 6F D2 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `3920C985-F404-4392-A642-11EC49EA0666
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 14 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3334.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;432B5C7C-F354-480B-A789-04C98084AFCB\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 34 33 32 42 35 43 37 43 2D 46 33 35 34 2D 34 38 30 '}`

### 31. `IMG_3335.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3335.PNG`
- **SHA-256:** `b4f1b5d8d4c50c6ae7b272f73d1072bf14e8d0eee4b146eadee1419abe643417`
- **Size:** 517,206 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:50 / 2026-08-07 17:06:50Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:50 / 2026-08-07 17:06:50Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:50</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:50 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:50 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:50 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:50 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 517206
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '48 8C FA 30 56 D3 40 0A AB CC CD 97 BD E1 09 48'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 15 31 A3 E4 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `488CFA30-56D3-400A-ABCC-CD97BDE10948
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 15 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3335.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;402FCA33-A432-45D2-BF90-C9623C96D03A\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 34 30 32 46 43 41 33 33 2D 41 34 33 32 2D 34 35 44 '}`

### 32. `IMG_3336.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3336.PNG`
- **SHA-256:** `fb098e752fe5a727a1b82bc3b14a48f893ecd914d5054fd77ed389a4828222a5`
- **Size:** 456,904 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:52 / 2026-08-07 17:06:52Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:52 / 2026-08-07 17:06:52Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:52</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:52 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:52 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:52 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:52 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 456904
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'F7 2C D4 F8 82 23 4E 8D B5 44 70 EA 80 9B F5 52'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 16 78 79 25 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `F72CD4F8-8223-4E8D-B544-70EA809BF552
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 16 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3336.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;F135A6CF-EFA4-434D-9A23-2F9BCD571DD2\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 46 31 33 35 41 36 43 46 2D 45 46 41 34 2D 34 33 34 '}`

### 33. `IMG_3337.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3337.PNG`
- **SHA-256:** `90d2cc09f85ede4d0d9d606cab685dbc50c853ef9614fe3cf4b84a9373daab62`
- **Size:** 511,895 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:54 / 2026-08-07 17:06:54Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:54 / 2026-08-07 17:06:54Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:54</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:54 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:54 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:54 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:54 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 511895
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'E1 95 CA 51 6E 87 4B C3 A8 0F 1F D3 7A CA 82 9F'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 17 6A B0 FB 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `E195CA51-6E87-4BC3-A80F-1FD37ACA829F
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 17 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3337.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;3CE0B0B9-8E01-40E5-B036-2056A91BFA85\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 33 43 45 30 42 30 42 39 2D 38 45 30 31 2D 34 30 45 '}`

### 34. `IMG_3338.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3338.PNG`
- **SHA-256:** `d001c7de3c4855133ac8722f11a6842989c35833e89c31d752a4a0feb7f03638`
- **Size:** 521,289 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:56 / 2026-08-07 17:06:56Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:56 / 2026-08-07 17:06:56Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:56</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:56 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:56 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:56 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:56 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 521289
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '39 3E 48 7B 15 74 42 12 80 50 18 41 67 6A 9B 12'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 18 5B F8 EC 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `393E487B-1574-4212-8050-1841676A9B12
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 18 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3338.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;EE2F9FB6-908E-4E99-90FB-C30CEA4045AF\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 45 45 32 46 39 46 42 36 2D 39 30 38 45 2D 34 45 39 '}`

### 35. `IMG_3339.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3339.PNG`
- **SHA-256:** `fb3de90c23e180e4f2f9efbd44fb294cda2ddede9a7283586e11165e060550e5`
- **Size:** 487,305 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:06:59 / 2026-08-07 17:06:59Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:06:59 / 2026-08-07 17:06:59Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:06:59</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:06:59 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:06:59 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:06:59 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:06:59 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 487305
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '0C 84 E1 73 74 30 41 B6 A5 58 28 33 17 65 BD 3B'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1A 06 F9 D3 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `0C84E173-7430-41B6-A558-28331765BD3B
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 19 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3339.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;341357FC-FF9D-4402-A272-EDDEB01D480D\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 33 34 31 33 35 37 46 43 2D 46 46 39 44 2D 34 34 30 '}`

### 36. `IMG_3340.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3340.PNG`
- **SHA-256:** `55ee702047cefd318b8e51d65f0f1901715b014349bc7a666abcd3e63540dfb6`
- **Size:** 441,869 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:02 / 2026-08-07 17:07:02Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:02 / 2026-08-07 17:07:02Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:02</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:02 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:02 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:02 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:02 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 441869
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'EE 2F F8 F6 05 FE 45 EE B4 77 E3 8F F5 07 C2 E6'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1B 23 D0 74 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `EE2FF8F6-05FE-45EE-B477-E38FF507C2E6
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1B 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3340.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;F96B0EF3-0FDB-44DF-8E4A-3C0D9094C8A3\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 46 39 36 42 30 45 46 33 2D 30 46 44 42 2D 34 34 44 '}`

### 37. `IMG_3341.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3341.PNG`
- **SHA-256:** `256ef7154c6c1947b0799b52993d070e75388dcb33f1e7992a2bd7764f39fd5a`
- **Size:** 436,920 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:04 / 2026-08-07 17:07:04Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:04 / 2026-08-07 17:07:04Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:04</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:04 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:04 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:04 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:04 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 436920
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '2C 87 83 24 1B 9B 43 F3 BC 49 E9 03 FB B0 0C AA'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1C 19 75 D1 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `2C878324-1B9B-43F3-BC49-E903FBB00CAA
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1C 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3341.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;CD50FE66-D4F1-4A91-A787-959F0A592565\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 43 44 35 30 46 45 36 36 2D 44 34 46 31 2D 34 41 39 '}`

### 38. `IMG_3342.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3342.PNG`
- **SHA-256:** `47f5b2beed02ee0f2cf45fb810016803331fe9386a8636347968918a534ba521`
- **Size:** 455,439 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:06 / 2026-08-07 17:07:06Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:06 / 2026-08-07 17:07:06Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:06</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:06 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:06 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:06 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:06 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 455439
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '5F DF 13 52 A7 17 45 65 AB 08 56 C3 BD C0 EA 0D'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1D 10 E6 EB 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `5FDF1352-A717-4565-AB08-56C3BDC0EA0D
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1D 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3342.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;9BD6AD51-6B29-452C-8E99-F80145787D0B\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 39 42 44 36 41 44 35 31 2D 36 42 32 39 2D 34 35 32 '}`

### 39. `IMG_3343.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3343.PNG`
- **SHA-256:** `871bfb81ec9de2427854e60d660c8091362d4d6bb87b4bfd3762799ff42ece4d`
- **Size:** 457,682 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:08 / 2026-08-07 17:07:08Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:08 / 2026-08-07 17:07:08Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:08</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:08 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:08 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:08 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:08 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 457682
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'B5 BB A4 EA 2B C3 44 3F 9B AA D3 9C 1E 55 26 CD'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1E 11 3D 53 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `B5BBA4EA-2BC3-443F-9BAA-D39C1E5526CD
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1E 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3343.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;6A488AEC-DF7E-42F2-AE7F-52096556BF5D\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 36 41 34 38 38 41 45 43 2D 44 46 37 45 2D 34 32 46 '}`

### 40. `IMG_3344.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3344.PNG`
- **SHA-256:** `f10046f921f4dd1b6c8c71f326373434956d9b0d830b7239f9ffed7959b5fa7b`
- **Size:** 471,544 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:10 / 2026-08-07 17:07:10Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:10 / 2026-08-07 17:07:10Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:10</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:10 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:10 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:10 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:10 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 471544
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '96 42 A3 A3 B0 4D 4A C9 92 F8 BD C9 AF 58 49 53'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1F 13 31 0A 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `9642A3A3-B04D-4AC9-92F8-BDC9AF584953
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1F 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3344.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;CFDA81CE-1A0F-44E5-9B26-04D87D94CED3\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 43 46 44 41 38 31 43 45 2D 31 41 30 46 2D 34 34 45 '}`

### 41. `IMG_3345.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3345.PNG`
- **SHA-256:** `e5bea6a3005208c3c4cfe3506a733646a5607f9083ccf19695eac0d9ff19cc96`
- **Size:** 469,773 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:11 / 2026-08-07 17:07:11Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:11 / 2026-08-07 17:07:11Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:11</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:11 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:11 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:11 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:11 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 469773
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'CD EE 25 A2 E2 C3 46 80 A0 66 D6 6A FE 72 44 45'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 20 04 03 8A 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `CDEE25A2-E2C3-4680-A066-D66AFE724445
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 1F 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3345.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;3A2373FC-E7DA-442A-A2D1-CE087E465FE4\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 33 41 32 33 37 33 46 43 2D 45 37 44 41 2D 34 34 32 '}`

### 42. `IMG_3346.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3346.PNG`
- **SHA-256:** `26caf788c9ae3a07030e46e905a88e8eccfb677aba036064c0c408430b70d1ea`
- **Size:** 455,903 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:16 / 2026-08-07 17:07:16Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:16 / 2026-08-07 17:07:16Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:16</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:16 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:16 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:16 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:16 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 455903
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '44 7D CB F5 E5 27 4F 77 A2 85 64 D8 90 F6 86 E1'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 22 13 EC 81 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `447DCBF5-E527-4F77-A285-64D890F686E1
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 22 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3346.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;C94A310E-6EBC-4FD4-8EA7-15CF06F843E5\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 43 39 34 41 33 31 30 45 2D 36 45 42 43 2D 34 46 44 '}`

### 43. `IMG_3347.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3347.PNG`
- **SHA-256:** `9ed00b4898ae60ce5eb2be55c7ac9753c56f79ab74ea69c9a8e77324ebff0715`
- **Size:** 473,357 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:18 / 2026-08-07 17:07:18Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:18 / 2026-08-07 17:07:18Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:18</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:18 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:18 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:18 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:18 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 473357
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'D9 69 BA 5E 09 1E 44 FC 95 5F 97 2C 49 B1 95 BB'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 23 87 56 3B 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `D969BA5E-091E-44FC-955F-972C49B195BB
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 23 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3347.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;ACE90FCB-D00B-42B4-80D8-0B99FE808E4F\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 41 43 45 39 30 46 43 42 2D 44 30 30 42 2D 34 32 42 '}`

### 44. `IMG_3348.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3348.PNG`
- **SHA-256:** `ed2b6b4e1fb1d2e1ddb6049d4b4254cebec9674d7ce319308f1fb6547d9c476c`
- **Size:** 467,646 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:21 / 2026-08-07 17:07:21Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:21 / 2026-08-07 17:07:21Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:21</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:21 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:21 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:21 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:21 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 467646
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '33 22 31 FC 22 0B 47 40 88 CF 2E 84 84 21 DB 74'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 24 C8 69 49 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `332231FC-220B-4740-88CF-2E848421DB74
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 24 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3348.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;0281FA64-1705-401A-B7E6-80A2F14809E7\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 30 32 38 31 46 41 36 34 2D 31 37 30 35 2D 34 30 31 '}`

### 45. `IMG_3349.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3349.PNG`
- **SHA-256:** `58811eff200e26d779c4230e53bd06525d5e4cce5d24be3ec4923469c005c2cd`
- **Size:** 497,240 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:23 / 2026-08-07 17:07:23Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:23 / 2026-08-07 17:07:23Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:23</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:23 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:23 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:23 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:23 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 497240
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'A0 8C 58 98 97 8E 48 FE 8C DB D9 59 62 63 EE 1E'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 25 F3 E2 69 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `A08C5898-978E-48FE-8CDB-D9596263EE1E
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 25 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3349.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;C5C48AD5-EF98-4ECA-AF80-AB610B0F2CDD\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 43 35 43 34 38 41 44 35 2D 45 46 39 38 2D 34 45 43 '}`

### 46. `IMG_3350.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3350.PNG`
- **SHA-256:** `74d196529d41f9ea2b92de3f0e67a063deee4a6df8c438a0ecab6af8cb0516c0`
- **Size:** 514,994 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:26 / 2026-08-07 17:07:26Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:26 / 2026-08-07 17:07:26Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:26</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:26 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:26 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:26 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:26 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 514994
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '31 1F B3 5E 21 6E 4D B9 8C BC 75 C3 89 AC 83 84'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 27 30 D2 C4 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `311FB35E-216E-4DB9-8CBC-75C389AC8384
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 27 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3350.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;A36A74A3-C3BC-41EF-AD9D-D22BC2550F7A\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 41 33 36 41 37 34 41 33 2D 43 33 42 43 2D 34 31 45 '}`

### 47. `IMG_3351.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3351.PNG`
- **SHA-256:** `3c926dd23da799c6cff6906e8a6e724f6865af248496e0791d4a0832617c0211`
- **Size:** 455,690 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:28 / 2026-08-07 17:07:28Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:28 / 2026-08-07 17:07:28Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:28</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:28 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:28 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:28 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:28 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 455690
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '1F 6F E6 1C FF 01 4D 76 9F 70 CC B2 A1 5F AC AA'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 28 4C 75 0C 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `1F6FE61C-FF01-4D76-9F70-CCB2A15FACAA
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 28 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3351.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;310AD788-F825-4055-84AE-5089E8061E0F\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 33 31 30 41 44 37 38 38 2D 46 38 32 35 2D 34 30 35 '}`

### 48. `IMG_3352.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3352.PNG`
- **SHA-256:** `bd715d65667db81531814a179d72bd12b7f7bd5df51c3edabcb6e67a6f1c1594`
- **Size:** 507,399 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:31 / 2026-08-07 17:07:31Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:31 / 2026-08-07 17:07:31Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:31</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:31 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:31 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:31 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:31 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 507399
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'EB E6 5A 39 6A ED 40 B5 92 0B D3 13 0B E1 A4 D6'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 29 B6 3F 03 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `EBE65A39-6AED-40B5-920B-D3130BE1A4D6
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 29 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3352.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;372CC418-C7A1-4728-98B0-6D3686397498\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 33 37 32 43 43 34 31 38 2D 43 37 41 31 2D 34 37 32 '}`

### 49. `IMG_3353.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3353.PNG`
- **SHA-256:** `7ad94a4d10b415df2b9228fa21f21f962e4b7b56fb7c2843372253502480590d`
- **Size:** 484,538 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:33 / 2026-08-07 17:07:33Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:33 / 2026-08-07 17:07:33Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:33</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:33 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:33 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:33 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:33 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 484538
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '8F 3B E9 99 0F 22 4F D1 98 7A BA 56 A6 9A 7C CC'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 2A B9 67 3C 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `8F3BE999-0F22-4FD1-987A-BA56A69A7CCC
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 2A 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3353.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;D65CE527-F177-41FA-ACE7-22D11C597C3E\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 44 36 35 43 45 35 32 37 2D 46 31 37 37 2D 34 31 46 '}`

### 50. `IMG_3354.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3354.PNG`
- **SHA-256:** `b5388773afb85df91f15d7b276db011e48f4a3d4de5947c25fb06b50571c62bc`
- **Size:** 400,140 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:35 / 2026-08-07 17:07:35Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:35 / 2026-08-07 17:07:35Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:35</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:35 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:35 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:35 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:35 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 400140
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'CB D2 30 7E 4E 43 44 8C 8F 1E BF C6 BE B9 56 CE'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 2B C2 C3 DB 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `CBD2307E-4E43-448C-8F1E-BFC6BEB956CE
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 2B 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3354.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;0097800B-7608-42DD-B042-87702E244C7C\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 30 30 39 37 38 30 30 42 2D 37 36 30 38 2D 34 32 44 '}`

### 51. `IMG_3355.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3355.PNG`
- **SHA-256:** `d75b5ac82795db95d8993604e1fb9c4af4b01463d641a32d6d5c65d889a9585a`
- **Size:** 420,553 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:38 / 2026-08-07 17:07:38Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:38 / 2026-08-07 17:07:38Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:38</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:38 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:38 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:38 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:38 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 420553
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': 'A3 89 ED 57 FB BE 47 9A AE E6 29 59 8F 13 40 A9'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 2D 14 0E B6 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `A389ED57-FBBE-479A-AEE6-29598F1340A9
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 2D 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3355.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;78ADD910-C776-4E1A-9853-92A1E2D46D30\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 37 38 41 44 44 39 31 30 2D 43 37 37 36 2D 34 45 31 '}`

### 52. `IMG_3356.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3356.PNG`
- **SHA-256:** `7a5535efc9d736a047a2e53783aa6441f7f5255ade770f2bcf2c41c0e7d29f88`
- **Size:** 484,856 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:40 / 2026-08-07 17:07:40Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:40 / 2026-08-07 17:07:40Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:40</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:40 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:40 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:40 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:40 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 484856
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '22 68 9C E4 78 EC 4F 16 8A 54 D8 1A 64 E7 19 DA'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 2E 27 9C FA 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `22689CE4-78EC-4F16-8A54-D81A64E719DA
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 2E 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3356.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;1125DBA9-C4A3-4EE0-81E4-0FC784C60F4E\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 31 31 32 35 44 42 41 39 2D 43 34 41 33 2D 34 45 45 '}`

### 53. `IMG_3357.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3357.PNG`
- **SHA-256:** `12032fd3eccca4cf5a9a6e96154ef4dda19bc6b69f73dde5150a27d9ae102ce9`
- **Size:** 522,303 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:42 / 2026-08-07 17:07:42Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:42 / 2026-08-07 17:07:42Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:42</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:42 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:42 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:42 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:42 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 522303
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '1F A7 66 7F AA AD 4D 80 BE 1C E4 3E 88 AD 47 49'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 2F 26 2D 95 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `1FA7667F-AAAD-4D80-BE1C-E43E88AD4749
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 2F 00 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3357.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;C091CE3C-EF19-41EC-AC72-7CA4B2A8F727\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 43 30 39 31 43 45 33 43 2D 45 46 31 39 2D 34 31 45 '}`

### 54. `IMG_3358.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3358.PNG`
- **SHA-256:** `f4159cfe4f295825b3b9baae331d8ae9a32099403182bc94de903428cccf2c91`
- **Size:** 532,686 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:07:45 / 2026-08-07 17:07:45Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:07:45 / 2026-08-07 17:07:45Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 8, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (142 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:07:45</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'sRGB', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '8', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'sRGB IEC61966-2.1'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:07:45 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:07:45 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:07:45 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:07:45 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "sRGB IEC61966-2.1"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 532686
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '33 9D EF 38 E4 52 40 D2 84 12 9C 53 40 7B A0 34'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 30 DA F0 D0 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `339DEF38-E452-40D2-8412-9C53407BA034
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 30 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3358.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;0014787D-2730-4031-8D5E-D93F0B29AF12\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 30 30 31 34 37 38 37 44 2D 32 37 33 30 2D 34 30 33 '}`

### 55. `IMG_3359.PNG`

- **Absolute path:** `/Users/hattr/Downloads/Proof RIP/IMG_3359.PNG`
- **SHA-256:** `93dbc26c54828d1cfef0ac615a2ff755da7a5a4d8ef6638735b75adc6e05eba3`
- **Size:** 2,569,646 bytes
- **Filesystem birthtime (local / UTC):** 2026-08-08 01:13:19 / 2026-08-07 17:13:19Z
- **Filesystem mtime (local / UTC):** 2026-08-08 01:13:19 / 2026-08-07 17:13:19Z
- **Metadata change ctime (local):** 2026-08-08 01:16:16
- **PNG IHDR:** {'width': 1284, 'height': 2778, 'bit_depth': 16, 'color_type': 2, 'compression': 0, 'filter': 0, 'interlace': 0}
- **PNG tIME chunk:** *(none)*
- **PNG eXIf present:** True (130 bytes)
- **PNG text keys:** {'XML:com.adobe.xmp': '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">\n   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n      <rdf:Description rdf:about=""\n            xmlns:exif="http://ns.adobe.com/exif/1.0/"\n            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">\n         <exif:UserComment>Screenshot</exif:UserComment>\n         <photoshop:DateCreated>2026-08-08T01:13:19</photoshop:DateCreated>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n'}
- **PNG pHYs:** None
- **PNG chunk types (order):** `['IHDR', 'iCCP', 'cICP', 'eXIf', 'iTXt', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IDAT', 'IEND']`
- **sips:** `{'pixelWidth': '1284', 'pixelHeight': '2778', 'typeIdentifier': 'public.png', 'format': 'png', 'formatOptions': 'default', 'dpiWidth': '72.000', 'dpiHeight': '72.000', 'samplesPerPixel': '3', 'bitsPerSample': '16', 'hasAlpha': 'no', 'space': 'RGB', 'profile': 'Display P3'}`
- **Spotlight (mdls) key fields:**
  - `kMDItemContentCreationDate` = 2026-08-07 17:13:19 +0000
  - `kMDItemContentModificationDate` = 2026-08-07 17:13:19 +0000
  - `kMDItemDateAdded` = 2026-08-07 17:16:16 +0000
  - `kMDItemFSCreationDate` = 2026-08-07 17:13:19 +0000
  - `kMDItemFSContentChangeDate` = 2026-08-07 17:13:19 +0000
  - `kMDItemDownloadedDate` = (null)
  - `kMDItemAcquisitionMake` = (null)
  - `kMDItemAcquisitionModel` = (null)
  - `kMDItemDeviceManufacturer` = (null)
  - `kMDItemDeviceModel` = (null)
  - `kMDItemWhereFroms` = (null)
  - `kMDItemCreator` = (null)
  - `kMDItemAuthors` = (null)
  - `kMDItemLatitude` = (null)
  - `kMDItemLongitude` = (null)
  - `kMDItemPixelWidth` = 1284
  - `kMDItemPixelHeight` = 2778
  - `kMDItemProfileName` = "Display P3"
  - `kMDItemColorSpace` = "RGB"
  - `kMDItemContentType` = "public.png"
  - `kMDItemKind` = "PNG image"
  - `kMDItemLogicalSize` = 2569646
  - `kMDItemTimestamp` = (null)
- **Extended attributes (xattr):** `['com.apple.assetsd.UUID', 'com.apple.assetsd.addedDate', 'com.apple.assetsd.assetType', 'com.apple.assetsd.avalanche.type', 'com.apple.assetsd.cloudAsset.UUID', 'com.apple.assetsd.creatorBundleID', 'com.apple.assetsd.currentSleetCast', 'com.apple.assetsd.customCreationDate', 'com.apple.assetsd.dbRebuildUuid', 'com.apple.assetsd.deferredProcessing', 'com.apple.assetsd.favorite', 'com.apple.assetsd.hidden', 'com.apple.assetsd.importedBy', 'com.apple.assetsd.importedByDisplayName', 'com.apple.assetsd.libraryScopeAssetContributorsToUpdate', 'com.apple.assetsd.libraryScopeShareState', 'com.apple.assetsd.originalFilename', 'com.apple.assetsd.sceneAnalysisIsFromPreivew', 'com.apple.assetsd.syndicationHistory', 'com.apple.assetsd.timeZoneName', 'com.apple.assetsd.timeZoneOffset', 'com.apple.assetsd.trashed', 'com.apple.assetsd.trashedReason', 'com.apple.assetsd.videoComplementVisibility', 'com.apple.assetsd.viewPresentation', 'com.apple.lastuseddate#PS', 'com.apple.macl', 'com.apple.quarantine']`
  - **com.apple.assetsd.UUID:** `{'hex_prefix': '38 86 B3 9A 26 19 4F 39 BA 37 71 56 82 DB 2E A3'}`
  - **com.apple.assetsd.addedDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 D7 B5 8F 04 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.assetType:** `
`
  - **com.apple.assetsd.avalanche.type:** `
`
  - **com.apple.assetsd.cloudAsset.UUID:** `3886B39A-2619-4F39-BA37-715682DB2EA3
`
  - **com.apple.assetsd.creatorBundleID:** `com.apple.springboard
`
  - **com.apple.assetsd.currentSleetCast:** `
`
  - **com.apple.assetsd.customCreationDate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 33 41 C8 13 24 D7 80 00 00 08 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11'}`
  - **com.apple.assetsd.dbRebuildUuid:** `46132AE3-2A83-4A8A-8B1C-2F6BD16FEA91
`
  - **com.apple.assetsd.deferredProcessing:** `
`
  - **com.apple.assetsd.favorite:** `
`
  - **com.apple.assetsd.hidden:** `
`
  - **com.apple.assetsd.importedBy:** `
`
  - **com.apple.assetsd.importedByDisplayName:** `SpringBoard
`
  - **com.apple.assetsd.libraryScopeAssetContributorsToUpdate:** `{'hex_prefix': '62 70 6C 69 73 74 30 30 D4 01 02 03 04 05 06 07 0A 58 24 76 65 72 73 69 6F 6E 59 24 61 72 63 68 69 76 65 72 54 24 74 6F 70 58 24 6F 62 6A 65 63 74 73 12 00 01 86 A0 5F 10 0F 4E 53 4B 65 79 65 64 41 72'}`
  - **com.apple.assetsd.libraryScopeShareState:** `
`
  - **com.apple.assetsd.originalFilename:** `IMG_3359.PNG
`
  - **com.apple.assetsd.sceneAnalysisIsFromPreivew:** `
`
  - **com.apple.assetsd.syndicationHistory:** `
`
  - **com.apple.assetsd.timeZoneName:** `Australia/Perth
`
  - **com.apple.assetsd.timeZoneOffset:** `{'hex_prefix': '80 70 00 00'}`
  - **com.apple.assetsd.trashed:** `
`
  - **com.apple.assetsd.trashedReason:** `
`
  - **com.apple.assetsd.videoComplementVisibility:** `
`
  - **com.apple.assetsd.viewPresentation:** `
`
  - **com.apple.lastuseddate#PS:** `:vj
`
  - **com.apple.macl:** `{'hex_prefix': '08 40 FC 73 BE AF 0F 1B 4D BE A9 6E 60 39 86 0B D2 2C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00', 'note': 'macOS privacy/provenance MAC label (binary)'}`
  - **com.apple.quarantine:** `{'text_or_plist': '0081;6a761239;sharingd;1C038F63-FFD6-4666-BC6A-01650EB92181\n', 'hex_prefix': '30 30 38 31 3B 36 61 37 36 31 32 33 39 3B 73 68 61 72 69 6E 67 64 3B 31 43 30 33 38 46 36 33 2D 46 46 44 36 2D 34 36 36 '}`

---

## Integrity verification

Recompute hashes later with:

```bash
cd "/Users/hattr/Downloads/Proof RIP" && shasum -a 256 IMG_*.PNG
```

Compare against the SHA-256 column above. Any mismatch means the file bytes changed after this log was made.

*Full machine-readable dump: `PROOF_RIP_METADATA_FULL.json`*