module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name = "neo-eks-cluster"
  cluster_version = "1.31"
  cluster_endpoint_public_access  = true

  subnet_ids = module.my-vpc.private_subnets
  vpc_id = module.my-vpc.vpc_id

  eks_managed_node_groups = {
    dev = {
      instance_types = ["t2.small"]
      min_size     = 1
      max_size     = 4
      desired_size = 2
    }
  }

  enable_cluster_creator_admin_permissions = true

  tags = {
    environment = var.env_prefix
    application = "neo-hazard-prediction"
  }
}