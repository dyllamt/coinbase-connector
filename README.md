## Contents

Up to date chart fields, defaults, and descriptions are documented with `helm-docs`.

## Usage

[Helm](https://helm.sh) must be installed to use the charts.  Please refer to
Helm's [documentation](https://helm.sh/docs) to get started.

Once Helm has been set up correctly, add the repo as follows:

    helm repo add cc https://dyllamt.github.io/coinbase-connector

If you had already added this repo earlier, to retrieve the latest versions of the packages:

    helm repo update cc

To see the charts:

    helm search repo cc

To install the coinbase-connector chart:

    helm install my-coinbase-connector cc/coinbase-connector

To uninstall the chart:

    helm delete my-coinbase-connector
