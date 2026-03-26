# AWS FastMemory Integration Template

## Architecture Map
```mermaid
graph LR
    User[End User] --> CloudFront[Amazon CloudFront]
    CloudFront --> Lambda[AWS Lambda / Fargate]
    Lambda --> Bedrock[Amazon Bedrock]
    Lambda --> FM_Fargate[FastMemory Service - ECS Fargate]
    FM_Fargate --> S3[Amazon S3 - ATF Store]
    FM_Fargate --> Neptune[(Amazon Neptune Graph)]
    FM_Fargate --> CloudWatch[Amazon CloudWatch]
```

## Integration Plan
1.  **Orchestration**: Use AWS Glue jobs to crawl S3 buckets and trigger FastMemory `build` via ECS Task.
2.  **Persistence**: High-frequency graph updates pipe into Amazon Neptune using the Gremlin/Cypher drivers.
3.  **Inference**: Integrate with AWS Bedrock (Claude 3.5 Sonnet) for deriving ontological relationships during `build`.
4.  **Security**: Map `A_` (Access) nodes to IAM Instance Profiles for granular service-to-service auth.
