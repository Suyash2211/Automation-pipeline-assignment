--- 

+++ 

@@ -2,9 +2,10 @@

   "account_id": "acc_637d5929",
   "company_name": "ABC Fire Protection",
   "business_hours": {
-    "days": "Mon-Fri",
-    "start": "09:00",
-    "end": "17:00"
+    "days": "all",
+    "start": "00:00",
+    "end": "23:59",
+    "timezone": "local"
   },
   "office_address": "",
   "services_supported": [
@@ -15,10 +16,14 @@

     "sprinkler leak",
     "fire alarm triggered"
   ],
-  "emergency_routing_rules": [],
+  "emergency_routing_rules": [
+    "transfer immediately to technician"
+  ],
   "non_emergency_routing_rules": [],
   "call_transfer_rules": {},
-  "integration_constraints": [],
+  "integration_constraints": [
+    "never create sprinkler jobs in ServiceTrade"
+  ],
   "after_hours_flow_summary": "",
   "office_hours_flow_summary": "",
   "questions_or_unknowns": [],