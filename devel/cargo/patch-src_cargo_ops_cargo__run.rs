--- src/cargo/ops/cargo_run.rs.orig	2016-08-21 22:32:57 UTC
+++ src/cargo/ops/cargo_run.rs
@@ -1,7 +1,7 @@
 use std::path::Path;
 
 use ops::{self, CompileFilter};
-use util::{self, CargoResult, process, ProcessError};
+use util::{self, CargoResult, ProcessError};
 use core::Package;
 
 pub fn run(manifest_path: &Path,
