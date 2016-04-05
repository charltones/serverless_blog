aws --profile vertu-ec2 s3 sync --exclude *~ --exclude *src* --exclude *misc* --exclude *less* --exclude *grunt* app s3://<your s3 bucket> --acl bucket-owner-full-control
