---
layout: default
title: China Readiness
description: How YANU separates global product pages from China compliance materials.
permalink: /compliance/
---

# China Readiness

**Last updated: July 29, 2026**

YANU keeps the global website and the mainland China edition separate because the product story and the compliance requirements are not the same thing.

The global site can stay product-led and English-first. The China edition needs Chinese-language materials for ICP filing, app filing, potential ICP licensing, domestic hosting, personal information protection disclosures, third-party service lists, and content governance.

## Current Structure

| Edition | Path | Purpose |
|---|---|---|
| Global | `/` | English product and brand foundation |
| China | `/cn/` | Chinese compliance-ready site for future domestic migration |

## Future China Deployment

When the domestic domain and access provider are ready, the China edition can be moved to a company-owned domain hosted by a mainland China cloud provider. At that point, the site should show the ICP filing number, app filing information, company details, and any required license notices.

## China Materials

- [中文中国版首页]({{ '/cn/' | relative_url }})
- [备案与许可说明]({{ '/cn/compliance/' | relative_url }})
- [隐私政策]({{ '/cn/privacy/' | relative_url }})
- [用户协议]({{ '/cn/terms/' | relative_url }})
- [个人信息清单]({{ '/cn/personal-info/' | relative_url }})
- [第三方服务清单]({{ '/cn/third-party-sdk/' | relative_url }})
