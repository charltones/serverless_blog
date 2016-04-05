aws --profile vertu-ec2 s3 sync --exclude *~ --exclude *src* --exclude *misc* --exclude *less* --exclude *grunt* app s3://sblog.vertulabs.co.uk --acl bucket-owner-full-control
