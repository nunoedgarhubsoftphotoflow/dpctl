.. _basic_concepts:

Basic Concepts
==============

The section introduces the basic concepts for XPU management used by dpctl.
As dpctl is based on SYCL the concepts should be familiar to users with prior
experience with SYCL. However, users of dpctl need not have any prior experience
with SYCL and the concepts presented here should be self-sufficient. We do not
go into all the SYCL-level details here and if needed readers should refer to a
more topical SYCL reference such as the :sycl_spec_2020:`SYCL 2020 spec <>`.

* **Heterogeneous computing**
    Refers to using multiple devices in a program.

* **Host**
    Every program starts by running on a host, and most of the lines of code in
    a program, in particular lines of code implementing the Python interpreter
    itself, are usually for the host. Hosts are customarily CPUs.

* **Device**
    A device is an XPU connected to a host that is programmable with a specific
    device driver. Different types of devices can have different architectures
    (CPUs, GPUs, FPGA, ASICs, DSP), but are programmable using the same
    :oneapi:`oneAPI <>` programming model.

* **Platform**
    A device driver installed on the system is termed as a platform. As multiple
    devices of the same type can share the same device driver, a platform may
    contain multiple devices. Note that the same physical hardware (say, a GPU)
    may be reflected as two separate devices if they can be programmed by more
    than one platform, *e.g.*, the same GPU hardware can be listed as an
    OpenCL GPU device and a Level-Zero GPU device.

* **Context**
   A context holds the run-time information needed to operate on a device or a
   group of devices from the same platform. Contexts are relatively expensive
   to create and should be reused as much as possible.

* **Queue**
   A queue is needed to schedule execution of any computation, or data
   copying on the device. Queue construction requires specifying a device
   and a context targeting that device as well as additional properties,
   such as whether profiling information should be collected or whether submitted
   tasks are executed in the order in which they were submitted.

* **Event**
   An event holds information related to computation/data movement operation
   scheduled for execution on a queue, such as its execution status as well
   as profiling information if the queue the task was submitted to allowed
   for collection of such information. Events can be used to specify task
   dependencies as well as to synchronize host and devices.

* **USM**
   Unified Shared Memory (USM) refers to pointer based device memory management.
   USM allocations are bound to context. In other words, a pointer representing
   USM allocation can be unambiguously mapped to the data it represents only
   if the associated context is known. USM allocations are accessible by
   computational kernels that are executed on a device, provided that the
   allocation is bound to the same context that was used to construct the queue
   where the kernel was scheduled for execution.

   Depending on the capability of the device, USM allocations can be a "device"
   allocation, a "shared" allocation, or a "host" allocation. A "device"
   allocation is not accessible from host, while "shared" or "host" allocations
   are. "Host" allocation refers to an allocation in host memory that is
   accessible from a device.

   "Shared" allocations are accessible by both host and device. Runtime manages
   synchronization of host's and device's view into shared allocations. Initial
   placement of the shared allocations is not defined.

* **Backend**
   Refers to an implementation of :oneapi:`oneAPI <>` programming model exposed
   by the underlying runtime.
