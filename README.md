# Adobe Document Intelligence Challenge – PDF Processor via Docker

##  Overview

This repository contains a PDF processing solution designed to extract structured data from documents. It includes:

- `Heading Extractor`: Parses a PDF and extracts clean title/subheading hierarchy while avoiding table data.
- `Persona Document Reader`: Reads specific persona-style documents and extracts structured fields like name, date of birth, address, etc.

Both utilities are containerized using Docker for reproducibility and portability.

---

##  Approach

### 1. Heading Extractor

- **Goal**: Extract hierarchical headings from scanned or digitally-created PDFs while avoiding noise like table headers, footers, and filler text.
- **Library**:PymuPDF
- **Logic**:
- Heading extraction
1.bold
2.Centered
3.underlined 
4.larger font size  than others
5.font styles
6.Capitalized
7. Whitesapces + positions 
8.colored 

-sub heading extraction
1.colon
2.numbers
3.boldded but lesser than title
4.Capitalized
5.underlined
6.bulleted ,asteriks
7.postion+whitespace

Outline List:
Heading (H1)
 |
 |
 v
Sub heading 1(H2)

....

Json format



### 2. Persona Document Reader

- **Goal**: Extract identity and attribute fields from semi-structured persona documents.
- **Logic**:
  - Used Bag of words like dictionary for collecting revelant words of text from the extracted pdf
  - When rate accuracy the words matched>90% and Take and collect that alone
  - Then give td-idf for identifying the rank related to the accuracy given
  - Then return the rank+relevant heading extracted from it.
{"type":"excalidraw/clipboard","workspaceId":"pAqxS8dIzGDDYih6zhrX","elements":[{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163559,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"CRq_O4ZKthQsN5-xpK27e","x":-200,"y":-607,"version":176,"versionNonce":1803430519,"elementStyle":0,"roughness":0,"shapeVersion":"v2","width":191,"height":67,"groupIds":["oPBjt1rd0T2WE63fjBF4O"],"lockedGroupId":"oPBjt1rd0T2WE63fjBF4O","seed":1765498297,"boundElementIds":["4JKScPEN68mpmIS31hRrR"],"zIndex":0,"isDeleted":false,"type":"rectangle","opacity":100,"angle":0,"shouldApplyRoughness":true,"diagramId":null,"containerId":null,"figureId":null,"fillStyle":"solid","backgroundColor":"transparent","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","colorMode":0},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163561,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"t7FpCH_Xxs1P38144nPKD","x":-195,"y":-583.5625,"version":84,"versionNonce":2103427991,"scale":0.875,"fontSize":20,"textAlign":"center","fontFamily":2,"mode":"normal","text":"Input files","roughness":0,"slate":[{"type":"paragraph","children":[{"text":"Input files"}]}],"verticalAlign":"middle","parentElementMetadata":{"elementId":"CRq_O4ZKthQsN5-xpK27e","type":"rectangle"},"width":180.98828125,"height":20.125,"groupIds":["oPBjt1rd0T2WE63fjBF4O"],"lockedGroupId":"oPBjt1rd0T2WE63fjBF4O","seed":518523991,"hasFixedBounds":true,"zIndex":1,"isDeleted":false,"type":"textbox","opacity":100,"angle":0,"shouldApplyRoughness":true,"boundElementIds":null,"diagramId":null,"containerId":null,"figureId":null,"backgroundColor":"transparent","fillStyle":"solid","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round"},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163567,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"4JKScPEN68mpmIS31hRrR","x":-104.5,"y":-538,"version":178,"versionNonce":852953559,"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":0,"strokeSharpness":"elbow","cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["down"],"segmentHandleManualPositions":{}},"points":[[0,0],[0,95]],"startBinding":{"elementId":"CRq_O4ZKthQsN5-xpK27e","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"fixed.CardinalDirection","direction":"down"},"portOrientation":"outward"},"width":0,"height":95,"seed":96622137,"zIndex":2,"isDeleted":false,"type":"arrow","opacity":100,"angle":0,"shouldApplyRoughness":true,"groupIds":[],"boundElementIds":null,"lockedGroupId":null,"diagramId":null,"containerId":null,"figureId":null,"lastCommittedPoint":null,"endBinding":null,"startArrowhead":null,"endArrowhead":"arrow","arrowHeadSize":12,"textGap":null,"gaps":[]},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163568,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"fCWCkAyVXYzKTpO-slvUv","x":-208,"y":-438,"version":416,"versionNonce":1929091225,"elementStyle":0,"roughness":0,"shapeVersion":"v2","width":208,"height":73.23185811803285,"groupIds":["JKfr_hHSRr3Bs7n4OJNdN"],"lockedGroupId":"JKfr_hHSRr3Bs7n4OJNdN","seed":425701657,"boundElementIds":["ksZulOpDhcgFb-sRhzerU","dgfQRfxG3rchAPg65EEly","01wAbAvGtlE59XNNmKwOQ"],"zIndex":3,"isDeleted":false,"type":"rectangle","opacity":100,"angle":0,"shouldApplyRoughness":true,"diagramId":null,"containerId":null,"figureId":null,"fillStyle":"solid","backgroundColor":"transparent","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","colorMode":0},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163616,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"Xfqk26Nb-kRSwVl0O1D3i","x":-202.998046875,"y":-420.1965709409836,"version":306,"versionNonce":270468697,"scale":0.875,"fontSize":20,"textAlign":"center","fontFamily":2,"mode":"normal","text":"Persona Input\n\n(like todo list for travel,etc)","roughness":0,"slate":[{"type":"paragraph","children":[{"text":"Persona Input"}]},{"type":"paragraph","children":[{"text":"(like todo list for travel,etc)"}]}],"verticalAlign":"middle","parentElementMetadata":{"elementId":"fCWCkAyVXYzKTpO-slvUv","type":"rectangle"},"width":197.99609375,"height":37.625,"groupIds":["JKfr_hHSRr3Bs7n4OJNdN"],"lockedGroupId":"JKfr_hHSRr3Bs7n4OJNdN","seed":1154586553,"hasFixedBounds":true,"zIndex":4,"isDeleted":false,"type":"textbox","opacity":100,"angle":0,"shouldApplyRoughness":true,"boundElementIds":null,"diagramId":null,"containerId":null,"figureId":null,"backgroundColor":"transparent","fillStyle":"solid","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round"},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163637,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"6-Bm6im3HDafP-cCTI-49","x":-549.6034556733232,"y":-227.2952444271267,"version":355,"versionNonce":229597209,"elementStyle":0,"roughness":0,"shapeVersion":"v2","width":138,"height":72,"groupIds":["_wcQO2EyfBfRx1n2hQDSk"],"lockedGroupId":"_wcQO2EyfBfRx1n2hQDSk","seed":186080247,"boundElementIds":["XaPIhbhc8H9Imi-POTa9X","dgfQRfxG3rchAPg65EEly","_4ZW8L8-qSQJXBmqC8LVv"],"zIndex":5,"isDeleted":false,"type":"rectangle","opacity":100,"angle":0,"shouldApplyRoughness":true,"diagramId":null,"containerId":null,"figureId":null,"fillStyle":"solid","backgroundColor":"transparent","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","colorMode":0},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163638,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"wVomVdkrdv4Vbw48VsVzt","x":-544.6034556733232,"y":-210.1077444271267,"version":135,"versionNonce":508721751,"scale":0.875,"fontSize":20,"textAlign":"center","fontFamily":2,"mode":"normal","text":"Relevant words\n\n(Bag of words","roughness":0,"slate":[{"type":"paragraph","children":[{"text":"Relevant words"}]},{"type":"paragraph","children":[{"text":"(Bag of words)"}]}],"verticalAlign":"middle","parentElementMetadata":{"elementId":"6-Bm6im3HDafP-cCTI-49","type":"rectangle"},"width":127.99609375,"height":37.625,"groupIds":["_wcQO2EyfBfRx1n2hQDSk"],"lockedGroupId":"_wcQO2EyfBfRx1n2hQDSk","seed":406028503,"hasFixedBounds":true,"zIndex":6,"isDeleted":false,"type":"textbox","opacity":100,"angle":0,"shouldApplyRoughness":true,"boundElementIds":null,"diagramId":null,"containerId":null,"figureId":null,"backgroundColor":"transparent","fillStyle":"solid","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round"},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163639,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"_4ZW8L8-qSQJXBmqC8LVv","x":-98.16789385164157,"y":-307.91765704611566,"version":470,"versionNonce":2091423801,"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":0,"strokeSharpness":"elbow","cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["left","down"]},"points":[[0,0],[-376.83210614835843,0],[-376.83210614835843,80.91765704611566]],"endBinding":{"elementId":"6-Bm6im3HDafP-cCTI-49","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"fixed.CustomPort","relativeOffset":[0.08120950251193039,-0.9917987659131471],"direction":"up"}},"width":376.83210614835843,"height":80.91765704611566,"seed":829631385,"zIndex":7,"figureId":"gAGAJr5ol3CcZBC8_TQOI","isDeleted":false,"type":"arrow","opacity":100,"angle":0,"shouldApplyRoughness":true,"groupIds":[],"boundElementIds":null,"lockedGroupId":null,"diagramId":null,"containerId":null,"lastCommittedPoint":null,"startBinding":null,"startArrowhead":null,"endArrowhead":"arrow","arrowHeadSize":12,"textGap":null,"gaps":[]},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753701969426,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"TvWCvS-BcfAS-uny1zgap","x":-252.6034556733232,"y":-53.295244427126704,"version":346,"versionNonce":191408265,"elementStyle":0,"roughness":0,"shapeVersion":"v2","width":138,"height":117.625,"groupIds":["yJLOJad1ZUC6DN0LXH4af"],"lockedGroupId":"yJLOJad1ZUC6DN0LXH4af","seed":1917133623,"boundElementIds":["XaPIhbhc8H9Imi-POTa9X","e4gtjgjlJgxCC1H3EtItN","zPD4CzxhDz4DYrowhx8TE"],"zIndex":8,"isDeleted":false,"type":"rectangle","opacity":100,"angle":0,"shouldApplyRoughness":true,"diagramId":null,"containerId":null,"figureId":null,"fillStyle":"solid","backgroundColor":"transparent","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","colorMode":0},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753701969422,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"5eyKVarH-4zW9tAs2twnz","x":-247.6034556733232,"y":-48.295244427126704,"version":199,"versionNonce":1420952935,"scale":0.875,"fontSize":20,"textAlign":"center","fontFamily":2,"mode":"normal","text":"When rate accuracy the words matched>90% \n\nTake and collect that alone","roughness":0,"slate":[{"type":"paragraph","children":[{"text":"When rate accuracy the words matched>90% "}]},{"type":"paragraph","children":[{"text":"Take and collect that alone"}]}],"verticalAlign":"middle","parentElementMetadata":{"elementId":"TvWCvS-BcfAS-uny1zgap","type":"rectangle"},"width":127.99609375,"height":107.625,"groupIds":["yJLOJad1ZUC6DN0LXH4af"],"lockedGroupId":"yJLOJad1ZUC6DN0LXH4af","seed":1278641399,"hasFixedBounds":true,"zIndex":9,"isDeleted":false,"type":"textbox","opacity":100,"angle":0,"shouldApplyRoughness":true,"boundElementIds":null,"diagramId":null,"containerId":null,"figureId":null,"backgroundColor":"transparent","fillStyle":"solid","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round"},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753701942907,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"XaPIhbhc8H9Imi-POTa9X","x":-409.6034556733232,"y":-191.2952444271267,"version":1737,"versionNonce":967130793,"points":[[0,0],[77.5,0],[77.5,196.8125],[155,196.8125]],"fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"elbow","backgroundColor":"#000","strokeColor":"#000000","cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["right","down","right"],"segmentHandleManualPositions":{}},"startBinding":{"elementId":"6-Bm6im3HDafP-cCTI-49","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"},"portOrientation":"outward"},"endBinding":{"elementId":"TvWCvS-BcfAS-uny1zgap","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"},"portOrientation":"outward"},"width":155,"height":196.8125,"seed":444272569,"zIndex":10,"isDeleted":false,"type":"arrow","opacity":100,"angle":0,"roughness":1,"shouldApplyRoughness":true,"groupIds":[],"boundElementIds":null,"lockedGroupId":null,"diagramId":null,"containerId":null,"figureId":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":"arrow","arrowHeadSize":12,"textGap":null,"gaps":[]},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753701947248,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"z7bJcs-rwkYOWO2qX4gA4","x":23.396544326676803,"y":-253.2952444271267,"version":358,"versionNonce":2134454503,"elementStyle":0,"roughness":0,"shapeVersion":"v2","width":138,"height":82.625,"groupIds":["Vgptb5DbvIYZLedlVykw4"],"lockedGroupId":"Vgptb5DbvIYZLedlVykw4","seed":1903438265,"boundElementIds":["e4gtjgjlJgxCC1H3EtItN","-GYZd2mxIzXWPSjPhozjz","01wAbAvGtlE59XNNmKwOQ"],"zIndex":11,"figureId":"gAGAJr5ol3CcZBC8_TQOI","isDeleted":false,"type":"rectangle","opacity":100,"angle":0,"shouldApplyRoughness":true,"diagramId":null,"containerId":null,"fillStyle":"solid","backgroundColor":"transparent","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","colorMode":0},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753701947247,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"laKTCqEkV9H1q0JBy8dt-","x":28.396544326676803,"y":-248.2952444271267,"version":144,"versionNonce":1626350121,"scale":0.875,"fontSize":20,"textAlign":"center","fontFamily":2,"mode":"normal","text":"Then give td-idf for identifying the rank related to the accuracy given","roughness":0,"slate":[{"type":"paragraph","children":[{"text":"Then give td-idf for identifying the rank related to the accuracy given"}]}],"verticalAlign":"middle","parentElementMetadata":{"elementId":"z7bJcs-rwkYOWO2qX4gA4","type":"rectangle"},"width":127.99609375,"height":72.625,"groupIds":["Vgptb5DbvIYZLedlVykw4"],"lockedGroupId":"Vgptb5DbvIYZLedlVykw4","seed":849202073,"hasFixedBounds":true,"zIndex":12,"isDeleted":false,"type":"textbox","opacity":100,"angle":0,"shouldApplyRoughness":true,"boundElementIds":null,"diagramId":null,"containerId":null,"figureId":null,"backgroundColor":"transparent","fillStyle":"solid","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round"},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753701942910,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"e4gtjgjlJgxCC1H3EtItN","x":-112.6034556733232,"y":5.517255572873296,"version":1204,"versionNonce":901773191,"points":[[0,0],[67,0],[67,-217.5],[134,-217.5]],"fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"elbow","backgroundColor":"#000","strokeColor":"#000000","cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["right","up","right"]},"startBinding":{"elementId":"TvWCvS-BcfAS-uny1zgap","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"endBinding":{"elementId":"z7bJcs-rwkYOWO2qX4gA4","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"width":134,"height":217.5,"seed":780610135,"zIndex":13,"isDeleted":false,"type":"arrow","opacity":100,"angle":0,"roughness":1,"shouldApplyRoughness":true,"groupIds":[],"boundElementIds":null,"lockedGroupId":null,"diagramId":null,"containerId":null,"figureId":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":"arrow","arrowHeadSize":12,"textGap":null,"gaps":[]},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163817,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"01wAbAvGtlE59XNNmKwOQ","x":-104,"y":-362.76814188196715,"version":1131,"versionNonce":1897288343,"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":0,"strokeSharpness":"elbow","cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["down","right","down"]},"points":[[0,0],[0,53.736448727420225],[182,53.736448727420225],[182,109.76814188196715]],"startBinding":{"elementId":"fCWCkAyVXYzKTpO-slvUv","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"fixed.CardinalDirection","direction":"down"}},"endBinding":{"elementId":"z7bJcs-rwkYOWO2qX4gA4","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"fixed.CustomPort","relativeOffset":[-0.20864556995183772,-0.9928533875430753],"direction":"up"}},"width":182,"height":109.76814188196715,"seed":1573341655,"zIndex":14,"figureId":"gAGAJr5ol3CcZBC8_TQOI","isDeleted":false,"type":"arrow","opacity":100,"angle":0,"shouldApplyRoughness":true,"groupIds":[],"boundElementIds":null,"lockedGroupId":null,"diagramId":null,"containerId":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":"arrow","arrowHeadSize":12,"textGap":null,"gaps":[]},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753701954652,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"B3U9a233zRHk0LnGUpqHh","x":437.7005830478252,"y":-121.2952444271267,"version":622,"versionNonce":2131166921,"elementStyle":0,"roughness":0,"shapeVersion":"v2","width":154.53844231067131,"height":117.69306930693074,"groupIds":["mpddnhK2ZEHECHe2P15vy"],"lockedGroupId":"mpddnhK2ZEHECHe2P15vy","seed":1017509401,"boundElementIds":["-GYZd2mxIzXWPSjPhozjz","ny_UO8portDBqPxhy0oh2","Cks42sjilEij4hE6VzBZZ"],"zIndex":15,"isDeleted":false,"type":"rectangle","opacity":100,"angle":0,"shouldApplyRoughness":true,"diagramId":null,"containerId":null,"figureId":null,"fillStyle":"solid","backgroundColor":"transparent","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","colorMode":0},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753701954647,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"Cp0TAERMk96qpQry6Pul7","x":442.7005830478252,"y":-98.76120977366134,"version":240,"versionNonce":126968615,"scale":0.875,"fontSize":20,"textAlign":"center","fontFamily":2,"mode":"normal","text":"Then return the rank+relevant heading extracted from it + \\optional  ","roughness":0,"slate":[{"type":"paragraph","children":[{"text":"Then return the rank+relevant heading extracted from it + optional  "}]}],"verticalAlign":"middle","parentElementMetadata":{"elementId":"B3U9a233zRHk0LnGUpqHh","type":"rectangle"},"width":144.53844231067131,"height":72.625,"groupIds":["mpddnhK2ZEHECHe2P15vy"],"lockedGroupId":"mpddnhK2ZEHECHe2P15vy","seed":1336818743,"hasFixedBounds":true,"zIndex":16,"isDeleted":false,"type":"textbox","opacity":100,"angle":0,"shouldApplyRoughness":true,"boundElementIds":null,"diagramId":null,"containerId":null,"figureId":null,"backgroundColor":"transparent","fillStyle":"solid","strokeColor":"#1c1c1c","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round"},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163830,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"-GYZd2mxIzXWPSjPhozjz","x":163.3965443266768,"y":-211.9827444271267,"version":2029,"versionNonce":1747321625,"points":[[0,0],[136.1520193605742,0],[136.1520193605742,149.53403465346537],[272.3040387211484,149.53403465346537]],"fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"elbow","backgroundColor":"#000","strokeColor":"#000000","cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["right","down","right"]},"startBinding":{"elementId":"z7bJcs-rwkYOWO2qX4gA4","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"endBinding":{"elementId":"B3U9a233zRHk0LnGUpqHh","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"width":272.3040387211484,"height":149.53403465346537,"seed":1097782263,"zIndex":17,"isDeleted":false,"type":"arrow","opacity":100,"angle":0,"roughness":1,"shouldApplyRoughness":true,"groupIds":[],"boundElementIds":null,"lockedGroupId":null,"diagramId":null,"containerId":null,"figureId":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":"arrow","arrowHeadSize":12,"textGap":null,"gaps":[]},{"modifiedBy":"-OW9IS88AGRAT4XBS1_l","modifiedAt":1753594163934,"userId":"MDpA6Bs7X8VmA8ZLUVLcmQzLf0M2","id":"Cks42sjilEij4hE6VzBZZ","x":70.10133691758915,"y":-308.10996473842334,"version":751,"versionNonce":1261576215,"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":0,"strokeSharpness":"elbow","cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["right","down"]},"points":[[0,0],[454.8025234370606,0],[454.8025234370606,186.26921873354914]],"endBinding":{"elementId":"B3U9a233zRHk0LnGUpqHh","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"fixed.CustomPort","relativeOffset":[0.12856420710541847,-1.0092699014642041],"direction":"up"}},"width":454.8025234370606,"height":186.26921873354914,"seed":1244763993,"zIndex":18,"figureId":"gAGAJr5ol3CcZBC8_TQOI","isDeleted":false,"type":"arrow","opacity":100,"angle":0,"shouldApplyRoughness":true,"groupIds":[],"boundElementIds":null,"lockedGroupId":null,"diagramId":null,"containerId":null,"lastCommittedPoint":null,"startBinding":null,"startArrowhead":null,"endArrowhead":"arrow","arrowHeadSize":12,"textGap":null,"gaps":[]}]}


---

##  Project Structure

adobe_heading_extractor/
├── app/
│ ├── extract_outline.py 
│ ├── utils.py # Any helper functions
├── input/ # Input PDFs
├── output/ # Output JSONs
├── main.py # Entry point
├── requirements.txt # All Python dependencies
├── Dockerfile # Container build file


##  How to Build and Run the Solution

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/adobe-heading-extractor.git
cd adobe-heading-extractor

##Build Docker Image
##Run Docker Container
task-1
docker build -t adobe-heading-extractor .
docker run --rm -v "%cd%/input:/app/input" -v "%cd%/output:/app/output" adobe-heading-extractor
docker run -v "%cd%/input:/app/input" -v "%cd%/output:/app/output" adobe-heading-extractor



task-2
docker build -t persona-doc-reader .
docker run --rm -v "%cd%/input:/app/input" -v "%cd%/output:/app/output" persona-doc-reader
docker run -d -v "%cd%/input:/app/input" -v "%cd%/output:/app/output" --name persona-container persona-doc-reader



##Output Format

task-1
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Section 1",
      "page": 1
    },
    ...
  ]
}

task-2
{
  "name": "John Doe",
  "dob": "01 Jan 2000",
  "gender": "Male",
  "address": "123 Street, City"
}
