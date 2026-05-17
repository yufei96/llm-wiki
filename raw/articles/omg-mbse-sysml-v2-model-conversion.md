---
title: "SysML v2 模型转换流程"
source: https://www.omgwiki.org/MBSE/doku.php?id=mbse:sysml_v2_transition:model_conversion_approach
date: 2026-05-17
tags: [MBSE, systems-engineering, OMG, INCOSE]
---

# SysML v2 模型转换流程

* [skip to content](#dokuwiki__content)

# [MBSE Wiki](/MBSE/doku.php?id=start "[H]")


* [Log In](/MBSE/doku.php?id=mbse:sysml_v2_transition:model_conversion_approach&do=login&sectok= "Log In")


* [Recent Changes](/MBSE/doku.php?id=mbse:sysml_v2_transition:model_conversion_approach&do=recent "Recent Changes [r]")
* [Media Manager](/MBSE/doku.php?id=mbse:sysml_v2_transition:model_conversion_approach&do=media&ns=mbse%3Asysml_v2_transition "Media Manager")
* [Sitemap](/MBSE/doku.php?id=mbse:sysml_v2_transition:model_conversion_approach&do=index "Sitemap [x]")

Trace: • [model\_conversion\_approach](/MBSE/doku.php?id=mbse:sysml_v2_transition:model_conversion_approach "mbse:sysml_v2_transition:model_conversion_approach")

---

mbse:sysml\_v2\_transition:model\_conversion\_approach


* [SysML v1 to SysML v2 Model Conversion Process](#sysml_v1_to_sysml_v2_model_conversion_process)
* [----](#section)
* [Other Considerations in the Model Conversion Process](#other_considerations_in_the_model_conversion_process)

[[Click Here]](http://www.omgwiki.org/MBSE/doku.php?id=mbse:sysml_v2_transition "http://www.omgwiki.org/MBSE/doku.php?id=mbse:sysml_v2_transition") to return to the INCOSE SysML v1 to SysML v2 Transition Guidance Activity Team Home Page

## SysML v1 to SysML v2 Model Conversion Process

[Download](https://www.de-bok.org/asset/5bd90f82fab101bdf093103f76ce74ec5411300e "https://www.de-bok.org/asset/5bd90f82fab101bdf093103f76ce74ec5411300e")

## ----

*Content derived from OUSW (R&E) publicly available material*

Figure 1 shows the steps in the conversion process from a SysML v1 model to a SysML v2 model which includes: (1) pre-process the SysML v1 model to prepare it for the transformation, (2) transform the SysML v1 model to a SysML v2 model, (3) post-process the SysML v2 model to better leverage the SysML v2 capabilities, and (4) validate that the SysML v2 model accurately reflects the intent of the SysML v1 model.

[![](/MBSE/lib/exe/fetch.php?media=mbse:sysml_v2_transition:sysml_v1_to_sysml_v2_model_conversion.png)](/MBSE/lib/exe/detail.php?id=mbse%3Asysml_v2_transition%3Amodel_conversion_approach&media=mbse:sysml_v2_transition:sysml_v1_to_sysml_v2_model_conversion.png "mbse:sysml_v2_transition:sysml_v1_to_sysml_v2_model_conversion.png") Figure 1 Model Conversion Process

In addition, further steps may be required to assess the impact of the SysML v2 model on existing artifacts that were derived from the SysML v1 model. The derived artifacts may need to be updated for the SysML v2 effort, but this is considered outside of the scope of the SysML v1 to SysML v2 model conversion. Each of these steps is summarized below.

#### Step 1 Pre-process the SysML v1 Model

This step involves pre-processing the SysML v1 model to prepare the model for transformation. The required pre-processing will depend on the transformation capability that the modeling tool provides, so it is important to understand the tool capability and limitations. Performing the standard SysML v1 to SysML v2 model transformation requires that the SysML v1 model conform to the SysML v1 specification, so the pre-processing should ensure that SysML v1 model conforms to its specification. Any tool-specific extensions along with other tool customizations to the model may need to be removed. However, the use of stereotypes and profiles are expected to be supported by the transformation.

Certain features of SysML v1, such as adjunct properties, are not incorporated in SysML v2. Part of the pre-processing could be to remove these elements or assess the impact of the transformation on these features and note that they may need to be addressed in the post-processing step.

Circular dependencies should be identified to determine if and how they may impact the transformation and addressed accordingly. The SysML v1 model may also need to be reorganized to enable an incremental conversion process.

Creating a well-formed SysML v1 model that conforms to good practice will facilitate the conversion process. Model validation errors should be resolved to ensure the model is well-formed. Standard modeling conventions should be applied such as consistent naming conventions and ambiguities and redundancies in the model should be minimized.

#### Step 2 Transform The SysML v1 Model to a SysML v2 Model

This step involves transforming the pre-processed SysML v1 model to a SysML v2 model. A SysML v1 model can be transformed to a SysML v2 model using a tool that can execute the standard SysML v1 to SysML v2 transformation specification. The standard transformation requires that the SysML v1 model be conformant to the SysML v1 specification to be transformed to a conformant SysML v2 model.

The SysML v1 to v2 transformation specification defines the rules for transforming each kind of element in SysML v1 to a corresponding element in SysML v2. The transformation also includes rules for cases where there is no corresp

[Content truncated — showing first 5,000 of 10,092 chars. LLM summarization timed out. To fix: increase auxiliary.web_extract.timeout in config.yaml, or use a faster auxiliary model. Use browser_navigate for the full page.]
